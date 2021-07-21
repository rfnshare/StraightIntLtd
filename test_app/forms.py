import json
from django import forms
from .models import *


class MyCustomForm(forms.ModelForm):
    class Meta:
        model = MyCustomModal
        fields = [
            'country',
            'state',
        ]

    def __init__(self, *args, **kwargs):
        super(MyCustomForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ChoiceField(choices=[('1','india'),('2','US')])
        self.fields['state'].queryset = State.objects.filter(pk=2)
