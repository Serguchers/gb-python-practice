from asyncio import QueueEmpty
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    print(queryset)
    template_name = 'products_list.html'