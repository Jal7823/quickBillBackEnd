from rest_framework import serializers
from ..models import Users


class SerializerClients(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'name', 'password']


class SerializerEmploye(serializers.ModelSerializer):

    def validate(self, data):
        data['role'] = 'employe'
        return data

    class Meta:
        model = Users
        fields = ['username', 'name', 'email', 'password']


