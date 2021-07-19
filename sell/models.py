from django.db import models

from customer import models as customer_models


class Invoice(models.Model):
    name = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    balance = models.IntegerField(null=True)
