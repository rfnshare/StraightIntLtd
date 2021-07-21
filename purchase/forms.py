from django import forms
from .models import *


class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.all()
        self.fields['supplier'].widget.attrs.update({'class': 'text-input form-control'})

    class Meta:
        model = Purchase
        fields = ['supplier']


class PurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['products'].queryset = Product.objects.filter(supplier_id=2)
        self.fields['products'].widget.attrs.update({'class': 'text-input form-control'})

    class Meta:
        model = Purchase
        fields = "__all__"
        exclude = ['supplier']
