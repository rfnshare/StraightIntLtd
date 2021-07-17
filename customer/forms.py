from django.forms import ModelForm
from django import forms
from .models import *


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Abdullah Al Faroque'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'rfnshare@gmail.com'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '75/4 East Maniknagar, Dhaka 1203'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '01521259370'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '38500'}),
            'uid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'rf45q8c'}),

        }


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('balance',)
        fields = "__all__"
