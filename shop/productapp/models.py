from django.db import models
from django.db.models import Manager
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default='1')
    objects = Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ManyToManyField(ProductCategory, default='', related_name='categories')
    site = models.ManyToManyField(Site, default='1')
    product_name = models.CharField(max_length=128)
    date_in = models.DateField()
    price = models.IntegerField()
    amount = models.IntegerField()
    supplier_name = models.CharField(max_length=128)
    objects = Manager()
    on_site = CurrentSiteManager('site')