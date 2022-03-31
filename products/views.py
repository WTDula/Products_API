from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

# Create your views here.

@api_view(["GET", "POST"])
def products_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(["GET"])
def products_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)