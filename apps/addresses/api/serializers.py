from rest_framework import serializers
from apps.addresses.models import Address
from core.api.serializers import UserWithoutPasswordSerializer


class AddressSerializer(serializers.ModelSerializer):
    user = UserWithoutPasswordSerializer(many=False, read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user']
