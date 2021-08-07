from rest_framework import serializers
from core.models import ApplicationUser


class UserWithoutPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ['id', 'first_name', 'last_name', 'username']
