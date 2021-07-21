from django import forms
from .models import *
from crispy_forms.helper import FormHelper


class CustomerCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['image'].required = False

    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ('is_deleted',)


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('balance', 'is_deleted')
        fields = "__all__"
