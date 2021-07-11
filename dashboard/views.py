from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'dashboard/dashboard.html')


def login(request):
    return render(request, 'dashboard/login.html')
