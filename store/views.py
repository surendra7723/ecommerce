from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Cart,CartItem
from .serializers import ProductSerializer, CartSerializer
@api_view()
def product_list(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
@api_view()
def product_detail(request,id):
    product=get_object_or_404(Product,pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)
@api_view()
def cart_list(request):
    carts=Cart.objects.all()
    serializer=CartSerializer(carts,many=True)
    return Response(serializer.data)
@api_view()
def cart_detail(request,id):
    cart=get_object_or_404(CartItem,pk=id)
    serializer=CartSerializer(cart)
    return Response(serializer.data)
    
    
    
    
  
        
  