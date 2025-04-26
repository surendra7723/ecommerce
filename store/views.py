from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from .filters import ProductFilter

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import status
from .models import Product, Collection,Review,Cart,CartItem,Customer
from .serializers import ProductSerializer, CollectionSerializer,ReviewSerializer,CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer,CustomerSerializer

from .pagination import DeafaultPagination

class ProductViewset(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=ProductFilter
    search_fields=['title','description']
    ordering_fields=['unit_price','last_update']
    pagination_class=DeafaultPagination
    
  
                         
    # def destroy(self, request, *args, **kwargs):
    #     if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
    #         return Response({'error':'product vannot be deleted because it is associated with orderitem'})
    #     return super().destroy(request,*args,**kwargs)
       
    def delete(self,request,pk):
        product=get_object_or_404(Product,pk=pk)
        if product.orderitems.count()>0:
            return Response({'error':'Product cant be deleted '})
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)
class CartViewset(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer  
         
class CartItemViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','post']
    def get_serializer_class(self):
        if self.request.method=="POST":
            return AddCartItemSerializer
        elif self.request.method=="PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer
    def get_queryset(self):
        return CartItem.objects \
                .filter(cart_id=self.kwargs['cart_pk']) \
                .select_related('product')
    
    
    
class CollectionViewset(ModelViewSet):
    queryset=Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class=CollectionSerializer
    def destroy(self,request,pk):
        collection=get_object_or_404(Collection,pk=pk)
        if collection.products.count()>0:
            return Response({'error':'Collection  cant be deleted '})
        collection.delete()
        return Response(status.HTTP_204_NO_CONTENT)
     
class ReviewViewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
        
class CustomerViewset(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    