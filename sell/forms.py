from django import forms

from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
