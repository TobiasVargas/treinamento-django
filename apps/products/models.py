from django.db import models


class Category(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProductImage(models.Model):
    file = models.FileField(upload_to="product_images")
