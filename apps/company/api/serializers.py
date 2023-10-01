from rest_framework import serializers
from ..models import Company


class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
