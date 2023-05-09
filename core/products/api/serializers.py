from rest_framework import serializers
from ..models import Brand,Category,Products,Provider

class SerializerProducts(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

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