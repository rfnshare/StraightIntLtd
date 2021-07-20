from django import forms
from .models import *


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
