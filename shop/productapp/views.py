from math import prod
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, ProductCategory
# Create your views here.

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    print(queryset)
    template_name = 'products_list.html'
    

def products(request, pk=None):
    
    if pk is None:
        products = Product.objects.all().prefetch_related('category')
    else:
        products = Product.objects.prefetch_related('category').filter(category__pk=pk).order_by('price')
    
    return render(request, 'products_list.html', {'object_list': products,
                                                  'categories': ProductCategory.objects.all()})