from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('carts',views.cart_list),
    path('carts/<int:id>/', views.cart_detail),
    
    
]
