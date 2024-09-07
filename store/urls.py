from django.urls import path

from rest_framework_nested import routers
from pprint import pprint

from . import views
router=routers.DefaultRouter()
router.register('products',views.ProductViewset,basename='products')
router.register('collections',views.CollectionViewset)
products_router=routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')
routers.NestedDefaultRouter(router,'products',lookup='product')
urlpatterns=router.urls + products_router.urls 

 
pprint(router.urls)

      

