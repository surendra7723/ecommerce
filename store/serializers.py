from decimal import  Decimal
from store.models import Product,Collection
from rest_framework import serializers

from decimal import  Decimal
from store.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.Serializer): 
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    collection=serializers.StringRelatedField(
        queryset=Collection.objects.all()
        )

   
  
class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    
    
    
  
    
    
    
     