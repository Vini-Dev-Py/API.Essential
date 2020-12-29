from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import ProductsItens, Customers, File
from .serializers import ProductsItensSerializer, CustomersSerializer, FileSerializer

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ProductsItensViewSet(viewsets.ModelViewSet):

    serializer_class = ProductsItensSerializer

    queryset = ProductsItens.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):

    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()

          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)