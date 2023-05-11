from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated

from ..models import Brand,Category,Products,Provider
from .serializers import SerializerBrand,SerializerCategory,SerializerProducts,SerializerProvider

from core.users.permisionsUsers import IsEmploye,is_Boss,is_Staff

@extend_schema_view(
    list=extend_schema(
        tags=['Products'],
        description='Should get all products'
    ),
    create=extend_schema(
        tags=['Products'],
        description='Create a new instance of Products',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Products'],
        description='Retrieve a specific instance of MyModel by ID',
        responses={
            200: SerializerProducts,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Products'],
        description='Update a specific instance of MyModel by ID',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Products'],
        description='Partial update a specific instance of MyModel by ID',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Products'],
        description='Delete a specific instance of MyModel by ID',
    ),
)
class ViewProducts(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = SerializerProducts    
    permission_classes = [IsEmploye]
@extend_schema_view(
    list=extend_schema(
        tags=['Category'],
        description='Should get all Category'
    ),
    create=extend_schema(
        tags=['Category'],
        description='Create a new instance of Category',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Category'],
        description='Retrieve a specific instance of Category',
        responses={
            200: SerializerCategory,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Category'],
        description='Update a specific instance of Category',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Category'],
        description='Partial update a specific instance of Category',
        request=SerializerProducts,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Category'],
        description='Delete a specific instance of Category',
    ),
)
class ViewCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SerializerCategory 
@extend_schema_view(
    list=extend_schema(
        tags=['Brand'],
        description='Should get all Brand'
    ),
    create=extend_schema(
        tags=['Brand'],
        description='Create a new instance of Brand',
        request=SerializerBrand,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Brand'],
        description='Retrieve a specific instance of Brand',
        responses={
            200: SerializerBrand,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Brand'],
        description='Update a specific instance of Brand',
        request=SerializerBrand,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Brand'],
        description='Partial update a specific instance of Brand',
        request=SerializerBrand,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Brand'],
        description='Delete a specific instance of Brand',
    ),
)
class ViewBrand(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = SerializerBrand 

@extend_schema_view(
    list=extend_schema(
        tags=['Provider'],
        description='Should get all Provider'
    ),
    create=extend_schema(
        tags=['Provider'],
        description='Create a new instance of Provider',
        request=SerializerProvider,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Provider'],
        description='Retrieve a specific instance of Provider',
        responses={
            200: SerializerProvider,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Provider'],
        description='Update a specific instance of Provider',
        request=SerializerProvider,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Provider'],
        description='Partial update a specific instance of Provider',
        request=SerializerProvider,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Provider'],
        description='Delete a specific instance of Provider',
    ),
)
class ViewProvider(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = SerializerProvider 