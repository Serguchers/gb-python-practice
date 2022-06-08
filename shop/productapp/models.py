from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ManyToManyField(ProductCategory, default='', related_name='categories')
    product_name = models.CharField(max_length=128)
    date_in = models.DateField()
    price = models.IntegerField()
    amount = models.IntegerField()
    supplier_name = models.CharField(max_length=128)