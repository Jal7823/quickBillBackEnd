from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema,extend_schema_view

from ..permisionsUsers import isStaff
from ..models import Users
from .serializers import SerializerUser,SerializerClients


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SerializerClients


    @extend_schema(
        tags=['Clients'],
        description='Create a new instance of users',
        request=SerializerClients,
        responses={
            201: 'The client was created successfully',
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    )

    def post(self, request):
        serializer = SerializerClients(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(
        tags=['Users'],
        description='Should get all users'
    ),
    create=extend_schema(
        tags=['Users'],
        description='Create a new instance of users',
        request=SerializerUser,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Users'],
        description='Retrieve a specific instance of MyModel by ID',
        responses={
            200: SerializerUser,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Users'],
        description='Update a specific instance of MyModel by ID',
        request=SerializerUser,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Users'],
        description='Partial update a specific instance of MyModel by ID',
        request=SerializerUser,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Users'],
        description='Delete a specific instance of MyModel by ID',
    ),
)
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
