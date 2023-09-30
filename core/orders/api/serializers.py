from rest_framework import serializers
from ..models import Orders, OrderItem


class SerializerOders(serializers.ModelSerializer):
    items = serializers.StringRelatedField()
    class Meta:
        model = Orders
        fields = '__all__'


class SerializerCreateOders(serializers.ModelSerializer):

    def validate(self, values):
        products = values['products']
        total = [i.price for i in products]
        values['total_amount'] = sum(total)
        return values

    class Meta:
        model = Orders
        fields = '__all__'


class SerializerOderItem(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
