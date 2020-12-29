from rest_framework import serializers
from .models import ProductsItens, Customers, File

class ProductsItensSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductsItens
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customers
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):

    class Meta:

        model = File

        ProductsItens.imageProducts = File.file

        fields = "__all__"

