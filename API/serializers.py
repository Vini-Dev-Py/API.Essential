from rest_framework import serializers
from .models import ProductsItens, Customers

class ProductsItensSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductsItens
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customers
        fields = '__all__'