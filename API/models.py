from django.db import models
from rest_framework import serializers
# from .models import File

# Create your models here.


def uploadImageProducts(instance, filename):

    return f"{instance.nameProducts} - {filename}"

class ProductsItens(models.Model):

    nameProducts = models.CharField(max_length=60)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    SKU = models.CharField(max_length=60)
    # image = models.ImageField(upload_to=uploadImageProducts, blank=True, null=True)
    imageProducts = models.CharField(max_length=100, blank=True, null=False)

class Customers(models.Model):

    nameCustomers = models.CharField(max_length=60)
    CPF = models.CharField(max_length=11)
    Email = models.CharField(max_length=60)
    Phone = models.PositiveBigIntegerField()
    End = models.CharField(max_length=60)


class Request(models.Model):

    nameCustomersRequest = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    CPF = models.CharField(max_length=11)
    date = models.CharField(max_length=60)
    price = models.PositiveBigIntegerField()
    numberRequest = models.CharField(max_length=10)
    CEP = models.CharField(max_length=60)
    endCustomersResquest = models.CharField(max_length=60)
    resquestItens = models.CharField(max_length=255)
    quantityItens = models.PositiveBigIntegerField()
    status = models.CharField(max_length=60)
    shippingMethod = models.CharField(max_length=60)

class File(models.Model):

    file = models.FileField(blank=False, null=False)

    def __str__(self):

        ProductsItens.imageProducts = self.file.name

        return self.file.name