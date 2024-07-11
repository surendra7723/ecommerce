from typing import Any
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils.html  import format_html,urlencode

from django.urls import reverse 

from django.http import HttpRequest
from . import models
class InventoryFilter(admin.SimpleListFilter):
    title="inventory"
    parameter_name = 'inventory'
    
    
    def lookups(self, request, model_admin): 
        return [
            ('<10','low')
            
        ]
    def queryset(self, request, queryset: QuerySet): 
        if self.value()=='<10':
            return queryset.filter(inventory__lt=10)
        
     
    
class TagInline(GenericTabularInline):
    model=TaggedItem
    autocomplete_fields=['tag']
@admin.register(models.Product)
class ProductAdmin (admin.ModelAdmin):
    inlines=[TagInline]  
    autocomplete_fields = ['collection']
    prepopulated_fields={"slug":["title"]}
    actions=["clear_inventory"]
    list_display = ['title', 'unit_price','inventory_status','collection_title'] 
    list_editable = ['unit_price']
    list_per_page = 100   
    list_filter = ['collection',"last_update",InventoryFilter]  # add filter by collection
    
    list_select_related = ['collection']
    search_fields=['first_name',"last_name"]
    def collection_title(self,product):
        return product.collection.title
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    @admin.action(description="clear_inventory")
    def clear_inventory(self,request,queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products inventory cleared successfully.",
            messages.ERROR
            )
        
        
        
@admin.action(description="Clear Inventory")   
def clear_inventory(self,request,queryset):
    updated_count=queryset.update(inventory=0) 
@admin.register(models.Collection)     
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
    @admin.display(ordering='products_count')
    def products_count(self,collection): 
        url=(
            reverse('admin:store_product_changelist')
            +'?'
            +urlencode({
               'collection__id':str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
    def get_queryset(self, request ) :
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name',"last_name","membership",'orders_count'] 
    list_editable = ['membership']
    list_per_page = 10
    ordering=['first_name',"last_name"]
    search_fields=['first_name__istartswith',"last_name__istartswith"]
    @admin.display(ordering="orders_count")
    def orders_count(self,customer):
        url=(
            reverse('admin:store_order_changelist')
            +'?'
            +urlencode({
               'customer__id':str(customer.id)
            }))
        return format_html('<a href="{}">{}</a>',url,customer.orders_count)
        
    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )
        

        
class OrderItemInline(admin.TabularInline):
        autocomplete_fields = ['product']
        model=models.OrderItem
        extra=0
        
@admin.register(models.Order)

class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines=[OrderItemInline]
    list_display  = ["id",'placed_at','customer'] 
    
    

# Register your models here.
 