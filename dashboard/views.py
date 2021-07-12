from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
    return render(request, 'dashboard/dashboard.html')


def login(request):
    return render(request, 'dashboard/login.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')
