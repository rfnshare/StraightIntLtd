from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.
from django.views import View
from django.views.generic import *


def index(request):
    return render(request, 'sell/create_sell.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    template_name = 'sell/create_sell.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('sell:list')


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'sell/sell_list.html'
