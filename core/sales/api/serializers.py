from rest_framework import serializers
from ..models import Sales
from core.products.api.serializers import SerializerProducts


class SerializersSales(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = SerializerProducts(many=True)

    class Meta:
        model = Sales
        fields = '__all__'


class SerializersCreateSales(serializers.ModelSerializer):

    def validate(self, value):
        data = value['products']
        total = [i.price for i in data]
        value['total_amount'] = sum(total)
        return value

    class Meta:
        model = Sales
        fields = ['user','products',]
