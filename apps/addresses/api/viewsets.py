from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from apps.addresses.api.serializers import CreateAddressSerializer, AddressSerializer
from apps.addresses.models import Address
from core.models import ApplicationUser
from core.pagination_classes import DefaultPagination


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
    http_method_names = ['get', 'post', 'head', 'options']
    pagination_class = DefaultPagination

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateAddressSerializer
        serializer = CreateAddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        address = Address()
        address.cep = serializer.data["cep"]
        address.city = serializer.data["city"]
        address.uf = serializer.data["uf"]
        address.street = serializer.data["street"]
        address.district = serializer.data["district"]
        address.number = serializer.data["number"]
        address.observations = serializer.data["observations"]
        address.user = request.user
        address.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def personalizated(self, request, *args, **kwargs):
        # print(self)
        # print(request)
        # print(Address.objects.all())
        # cons = Address.objects.filter(id=3)

        # id_query_string = request.GET.get("id", None)

        user = ApplicationUser.objects.first()
        print(user.address_set.all()[:2])

        return Response(status=status.HTTP_200_OK)
