from rest_framework import serializers
from ..models import Users


class SerializerClients(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude=['is_staff','is_superuser','last_login','is_active','date_joined','image','groups','user_permissions','role',]

class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


