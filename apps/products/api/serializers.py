from rest_framework import serializers
from ..models import Brand, Category, Products, Provider


class SerializerBrand(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SerializerProvider(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class SerializerProducts(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()
    category = SerializerCategory(many=True)
    brand = serializers.StringRelatedField()

    class Meta:
        model = Products
        fields = '__all__'


class SerializerCreateProducts(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def validate(self, data):
        wPrice = data.get('wPrice')
        if wPrice is not None:
            newPrice = wPrice * 1.25
            data['price'] = newPrice
        return data
