from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from core.users.permisionsUsers import isStaff
from ..models import Company
from .serializers import SerializerCompany


@extend_schema_view(
    list=extend_schema(
        tags=['Company'],
        description='Should get all Company'
    ),
    create=extend_schema(
        tags=['Company'],
        description='Create a new instance of Company',
        request=SerializerCompany,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['Company'],
        description='Retrieve a specific instance of Company by ID',
        responses={
            200: SerializerCompany,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['Company'],
        description='Update a specific instance of Company by ID',
        request=SerializerCompany,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['Company'],
        description='Partial update a specific instance of Company by ID',
        request=SerializerCompany,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['Company'],
        description='Delete a specific instance of Company by ID',
    ),
)
class ViewsCompany(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany
    permission_classes = [isStaff]

