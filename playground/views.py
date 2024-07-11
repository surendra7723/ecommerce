from django.shortcuts import render
from django.db import connection
from store.models import Order,OrderItem,Product,Customer

def say_hello(request):
   with connection.cursor() as cursor:
      cursor.callproc('get_costumers',[1,2,'a'])
   return render(request,'hello.html',{'name':'Surendra'}) 