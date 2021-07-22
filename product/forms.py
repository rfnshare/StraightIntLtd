from django import forms
from .models import *


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'novalidate ': 'novalidate '}))

    # def __init__(self, *args, **kwargs):
    #     super(ProductCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = False

    class Meta:
        model = Product
        fields = "__all__"
