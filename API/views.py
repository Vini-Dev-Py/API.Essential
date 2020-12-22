from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import ProductsItens, Customers
from .serializers import ProductsItensSerializer, CustomersSerializer

class ProductsItensViewSet(viewsets.ModelViewSet):

    serializer_class = ProductsItensSerializer
    queryset = ProductsItens.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):

    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()