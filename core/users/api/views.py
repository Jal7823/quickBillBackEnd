import jwt

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from drf_spectacular.utils import extend_schema


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=LoginSerializer,
    responses={200: UserSerializer},
    description='Authenticate user with credentials'
)
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data.get('credentials', {}))
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user:
            payload = {
                'id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, 'SECRET_KEY')
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)