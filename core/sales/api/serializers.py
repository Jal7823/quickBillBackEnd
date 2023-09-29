from rest_framework import serializers
from ..models import Sales
from core.products.api.serializers import SerializerProducts

class SerializersSales(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = SerializerProducts(many=True)
    class Meta:
        model = Sales
        fields = '__all__'
