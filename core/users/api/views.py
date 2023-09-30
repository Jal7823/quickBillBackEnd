from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from ..permisionsUsers import isStaff
from ..models import Users
from .serializers import SerializerClients, SerializerEmploye


@extend_schema_view(
    list=extend_schema(
        tags=['Employee'],
        description='Should get all Employee'
    ),
    create=extend_schema(
        tags=['Employee'],
        description='Create a new instance of Employee',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['Employee'],
        description='Retrieve a specific instance of Employee by ID',
        responses={
            200: SerializerEmploye,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['Employee'],
        description='Update a specific instance of Employee by ID',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['Employee'],
        description='Partial update a specific instance of Employee by ID',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['Employee'],
        description='Delete a specific instance of Employee by ID',
    ),
)
class RegisterEmploye(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role='employe')
    permission_classes = [AllowAny]
    serializer_class = SerializerEmploye

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(
        tags=['Clients'],
        description='Should get all Clients'
    ),
    create=extend_schema(
        tags=['Clients'],
        description='Create a new instance of Clients',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['Clients'],
        description='Retrieve a specific instance of Clients by ID',
        responses={
            200: SerializerClients,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['Clients'],
        description='Update a specific instance of Clients by ID',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['Clients'],
        description='Partial update a specific instance of Clients by ID',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['Clients'],
        description='Delete a specific instance of Clients by ID',
    ),
)
class RegisterClients(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role='clients')
    permission_classes = [AllowAny]
    serializer_class = SerializerClients

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            password = request.data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
