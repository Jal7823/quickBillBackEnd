from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.users.permisionsUsers import IsEmploye,IsStaff
from ..models import Sales
from .serializers import SerializersSales,SerializersCreateSales

@extend_schema_view(
    list=extend_schema(
        tags=['Sales'],
        description='Should get all products'
    ),
    create=extend_schema(
        tags=['Sales'],
        description='Create a new instance of Sales',
        request=SerializersCreateSales,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Sales'],
        description='Retrieve a specific instance of MyModel by ID',
        responses={
            200: SerializersSales,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Sales'],
        description='Update a specific instance of MyModel by ID',
        request=SerializersSales,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Sales'],
        description='Partial update a specific instance of MyModel by ID',
        request=SerializersSales,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Sales'],
        description='Delete a specific instance of MyModel by ID',
    ),
)
class ViewsSales(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SerializersSales


    def create(self, request, *args, **kwargs):
        serializer = SerializersCreateSales(data=request.data)
        if serializer.is_valid():
            sale = serializer.save()
            sale.refresh_from_db()
            return Response(self.get_serializer(sale).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
