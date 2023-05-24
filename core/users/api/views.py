import jwt

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate

from drf_spectacular.utils import extend_schema

from ..models import Users
from .serializers import SerializerUser

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SerializerUser

    def post(self, request):
        serializer = SerializerUser(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ViewUsers(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = SerializerUser
















































# @extend_schema(
#     request=LoginSerializer,
#     responses={200: SerializerUser},
#     description='Authenticate user with credentials'
# )
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data.get('credentials', {}))
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

#         user = authenticate(username=username, password=password)

#         if user:
#             payload = {
#                 'id': user.id,
#                 'username': user.username,
#             }
#             token = jwt.encode(payload, 'SECRET_KEY')
#             return Response({'token': token})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)