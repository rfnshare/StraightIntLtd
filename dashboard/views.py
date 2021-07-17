from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from customer.models import *
from sell.models import *
from django.views.generic import *
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Customer.objects.all()
        context['total_customer'] = Customer.objects.all().count()
        context['total_invoices'] = Invoice.objects.all().count()
        return context


