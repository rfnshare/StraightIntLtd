from django import forms
from .models import *


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
