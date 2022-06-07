from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=128)
    date_in = models.DateField()
    price = models.IntegerField()
    amount = models.IntegerField()
    supplier_name = models.CharField(max_length=128)