from django.db import models
from supplier.models import *
from product.models import *


# Create your models here.

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    purchase_no = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.supplier.name

