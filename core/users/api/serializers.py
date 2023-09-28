from rest_framework import serializers
from ..models import Users


class SerializerClients(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'name', 'password']


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
