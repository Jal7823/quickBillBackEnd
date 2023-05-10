from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import viewsets,status

from ..models import OrderItem,Orders
from .serializers import SerializerOders,SerializerOderItem



class ViewOrders(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = SerializerOders


class ViewOrderItems(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = SerializerOderItem