from rest_framework import serializers
from ..models import Orders,OrderItem

class SerializerOders(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class SerializerOderItem(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'