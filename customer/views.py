from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import *
# Create your views here.
from django.views import View
from .forms import *


def index(request):
    return render(request, 'customer/create_customer.html')


def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('customer:customer_list')
    ctx = {'form': form}
    return render(request, 'customer/create_customer.html', ctx)


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    paginate_by = 10

# class ProtectView(LoginRequiredMixin, View):
#     def get(self, request):
#         forms = CustomerForm()
#         ctx = {
#             'forms': forms
#         }
#         return render(request, 'customer/create_customer.html', ctx)
#
#     def post(self, request):
#         forms = CustomerForm()
#         ctx = {
#             'forms': forms
#         }
#         return render(request, 'customer/create_customer.html', ctx)
#         # if request.method == 'POST':
def customerDetails(request, pk):
    customer = Customer.objects.get(id=pk)
    form =CustomerForm(instance= customer)
    return render(request, "customer/customer_details.html",{'form':form})