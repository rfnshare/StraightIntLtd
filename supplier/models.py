from django.db import models


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name
