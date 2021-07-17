from django.contrib import admin

# Register your models here.
from sell.models import Invoice


@admin.register(Invoice)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
