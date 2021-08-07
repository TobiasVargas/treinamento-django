from django.contrib import admin
from apps.products.models import Category, ProductImage


admin.site.register(Category)
admin.site.register(ProductImage)

