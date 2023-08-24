
from rest_framework import viewsets,status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter



from ..models import OrderItem,Orders
from .serializers import SerializerOders,SerializerOderItem


@extend_schema_view(
    list=extend_schema(
        tags=['Orders'],
        description='Should get all orders'
    ),
    create=extend_schema(
        tags=['Orders'],
        description='Create a new instance of orders',
        request=SerializerOders,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    retrieve=extend_schema(
        tags=['Orders'],
        description='Retrieve a specific instance of MyModel by ID',
        responses={
            200: SerializerOders,
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    update=extend_schema(
        tags=['Orders'],
        description='Update a specific instance of MyModel by ID',
        request=SerializerOders,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    partial_update=extend_schema(
        tags=['Orders'],
        description='Partial update a specific instance of MyModel by ID',
        request=SerializerOders,
        responses={
            400: 'The information is missed',
            404: 'Not found',
            500: 'Internal server error',
        },
    ),
    destroy=extend_schema(
        tags=['Orders'],
        description='Delete a specific instance of MyModel by ID',
    ),
)
class ViewOrders(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = SerializerOders

class ViewOrderItems(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = SerializerOderItem


