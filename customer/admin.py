from django.contrib import admin
from .models import *

# Register your models here.


#admin.site.register(Customer)


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name', 'email', 'phone', 'address']
