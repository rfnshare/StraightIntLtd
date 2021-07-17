from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='admin_pic', default='avatar.jpg')

    def __str__(self):
        return self.staff.username
