from django import forms
from django.forms import ModelForm
from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
