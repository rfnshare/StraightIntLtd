# from django.shortcuts import render
#
# # Create your views here.

from django.shortcuts import render
from .forms import MyCustomForm
from .models import *


def regcar(request):
    car_form = MyCustomForm
    return render(request, 'core/regcar.html', {'car_form': car_form})
