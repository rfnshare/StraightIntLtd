from django import forms
from .models import *
from customer.models import Customer


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        # self.fields['name'].queryset = Customer.objects.values_list('uid')
        self.fields['name'].queryset = Customer.objects.all()
        self.fields['balance'].queryset = Customer.objects.filter(pk=2)
