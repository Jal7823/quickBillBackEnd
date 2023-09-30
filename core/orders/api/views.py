from rest_framework.response import Response
from rest_framework import viewsets,status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from ..models import OrderItem,Orders
from .serializers import SerializerOders,SerializerOderItem,SerializerCreateOders


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

    def create(self, request, *args, **kwargs):
        serializer = SerializerCreateOders(data=request.data)
        if serializer.is_valid():
            user =  request.user
            print(user)
            products = serializer.save()
            return Response(self.get_serializer(products).data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class ViewOrderItems(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = SerializerOderItem


