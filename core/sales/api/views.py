from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

from ..models import Sales
from .serializers import SerializersSales


class ViewsSales(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SerializersSales
