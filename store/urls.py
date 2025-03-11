from django.urls import path

from rest_framework_nested import routers
from pprint import pprint

from . import views
router=routers.DefaultRouter()
router.register('products',views.ProductViewset,basename='products')
router.register('collections',views.CollectionViewset)
router.register('carts',views.CartViewset)
products_router=routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')
# carts_router=routers.NestedDefaultRouter(router,'carts',lookup='cart')
# carts_router.register('carts',views.CartViewset,basename='carts')
carts_router=routers.NestedDefaultRouter(router,'carts',lookup='cart')
carts_router.register('items',views.CartItemViewSet,basename='cart-items')
router.register('customer',views.CustomerViewset)


urlpatterns=router.urls + products_router.urls +carts_router.urls

 
pprint(router.urls)

      

 