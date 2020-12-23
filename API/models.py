from django.db import models

# Create your models here.


def uploadImageProducts(instance, filename):

    return f"{instance.nameProducts} - {filename}"

class ProductsItens(models.Model):

    nameProducts = models.CharField(max_length=60)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to=uploadImageProducts, blank=True, null=True)

class Customers(models.Model):

    nameCustomers = models.CharField(max_length=60)
    CPF = models.PositiveBigIntegerField()
    Email = models.CharField(max_length=60)
    Phone = models.PositiveBigIntegerField()
    End = models.CharField(max_length=60)