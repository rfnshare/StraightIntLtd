# Create your models here.
from django.db import models
from supplier.models import Supplier


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True)
    buy_price = models.IntegerField(null=True)
    sell_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
