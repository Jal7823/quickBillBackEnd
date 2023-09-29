from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

from ..models import Sales
from .serializers import SerializersSales,SerializersCreateSales

@extend_schema_view(
    create=extend_schema(
        description='Create a new sale',
        request=SerializersSales,
        responses={
            201: SerializersSales,
            400: 'Bad Request',
        },
    ),
)
class ViewsSales(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SerializersSales
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = SerializersCreateSales(data=request.data)
        if serializer.is_valid():
            sale = serializer.save()
            sale.refresh_from_db()
            return Response(self.get_serializer(sale).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
