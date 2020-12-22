from django.db import models

# Create your models here.

class ProductsItens(models.Model):

    name = models.CharField(max_length=60)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()

class Customers(models.Model):

    name = models.CharField(max_length=60)
    CPF = models.PositiveBigIntegerField()
    Email = models.CharField(max_length=60)
    Phone = models.PositiveBigIntegerField()
    End = models.CharField(max_length=60)