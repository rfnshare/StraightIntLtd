from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
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
    form = CustomerForm(instance=customer)
    return render(request, "customer/customer_details.html", {'form': form})


class CustomerDetails(DetailView):
    model = Customer
    template_name = 'customer/customer_details.html'


"""def cuEdit(request, pk):
    customer = Customer.objects.get(id=pk)
    form =CustomerForm(instance= customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance = customer)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
    ctx = {'form': form}
    return render(request, 'customer/customer_edit.html', ctx)"""


class customer_edit(UpdateView):
    model = Customer
    template_name = 'customer/customer_edit.html'

    fields = [
        'name',
        'phone',
        'address',
        'balance'
    ]
    success_url = reverse_lazy('customer:customer_list')


"""def cuDelete(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm()
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:customer_list')
    ctx = {'form': form}
    return render(request, 'customer/customer_delete.html', ctx)"""


class customer_delete(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer:customer_list')
