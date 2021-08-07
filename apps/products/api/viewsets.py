from rest_framework import viewsets, permissions
from apps.products.models import Category
from apps.products.api.serializers import CategorySerializer
from core.authorization_classes import IsAdminOrReadOnly


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
