from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Customer(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    address = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    balance = models.IntegerField(default=0)
    uid = models.CharField(max_length=100, null=True, unique=True)
    image = models.ImageField(default='avartar.jpg', upload_to='customer_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
