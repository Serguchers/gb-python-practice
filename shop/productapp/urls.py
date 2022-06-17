from django.urls import path
import productapp.views as productapp

urlpatterns = [
    path('products/', productapp.products, name='products'),
    path('products/<int:pk>', productapp.products, name='products')
]
