from math import prod
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, ProductCategory
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.


def products(request, pk=None):
    
    if pk is None:
        products = Product.on_site.all().prefetch_related('category')
    else:
        products = Product.on_site.prefetch_related('category').filter(category__pk=pk).order_by('price')
    
    return render(request, 'products_list.html', {'object_list': products,
                                                  'categories': ProductCategory.objects.all(),
                                                  'site': get_current_site(request)})