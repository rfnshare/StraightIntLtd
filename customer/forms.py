from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import *
from django.core.validators import RegexValidator
from phonenumber_field.phonenumber import PhoneNumber


class CustomerCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter customer fullname'}),
                           validators=[validators.MinLengthValidator(2, "Please enter 2 or more characters")])
    uid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter UID'}), validators=[validators.MinLengthValidator(2, "Please enter 2 or more characters")])

    # phone = PhoneNumberField(
    #     widget=PhoneNumberPrefixWidget(initial='BD')
    # )

    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['image'].required = False

    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ('is_deleted', 'owner')


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('balance', 'is_deleted', 'owner')
        fields = "__all__"
