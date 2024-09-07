from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Collection,Review
from .serializers import ProductSerializer, CollectionSerializer,ReviewSerializer

class ProductViewset(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_filelds=['collection_id']
  
    
    def get_serializer_context(self):
        return {'request': self.request}
                         
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
            return Response({'error':'product vannot be deleted because it is associated with orderitem'})
        return super().destroy(request,*args,**kwargs)
       
        
    
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CollectionViewset(ModelViewSet):
    queryset=Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class=CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        collection=get_object_or_404(Collection,pk=pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ReviewViewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
        
      
    


    
    
        
        
    
    
        
        