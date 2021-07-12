from django.forms import ModelForm
from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)

    class Meta:
        model = Customer
        fields = "__all__"
