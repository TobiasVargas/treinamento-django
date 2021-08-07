from django.db import models

from core.models import ApplicationUser


class Address(models.Model):
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    number = models.CharField(max_length=50, null=True, blank=True, default='SN')
    observations = models.TextField(null=True, blank=True)

    user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)

    def __str__(self):
        return "Endereço do usuário " + self.user.username
