from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    balance = models.IntegerField()
    uid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
