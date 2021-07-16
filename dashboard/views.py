from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from customer.models import *

from django.views.generic import TemplateView
# Create your views here.
from django.views import View


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Customer.objects.all()
        return context

def index(request):
    return render(request, 'dashboard/dashboard.html')


def login(request):
    return render(request, 'dashboard/login.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        total_customer = Customer.objects.all().count()
        ctx = {
            'total_customer': total_customer
        }
        return render(request, 'dashboard/dashboard.html', ctx)
