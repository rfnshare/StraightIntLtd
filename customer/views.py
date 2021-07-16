from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import *
from django.contrib import messages
from django.views import View
from .forms import *


# class CustomerIndexView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    template_name = 'customer/create_customer.html'
    fields = [
        'name',
        'email',
        'phone',
        'address',
        'uid',
        'balance'
    ]
    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy('customer:customer_list')


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    paginate_by = 10


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = 'customer/customer_edit.html'

    fields = [
        'name',
        'email',
        'phone',
        'address',
        'uid'

    ]
    success_message = '%(name)s was updated successfully'
    success_url = reverse_lazy('customer:customer_list')


class CustomerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_message = '%(name)s was deleted successfully'
    success_url = reverse_lazy('customer:customer_list')


class CustomerDetailsView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer/customer_details.html'

# def create_customer(request):
#     form = CustomerForm()
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Customer Creation successful')
#             return redirect('customer:customer_list')
#     ctx = {'form': form}
#     return render(request, 'customer/create_customer.html', ctx)
#
#
# def cuEdit(request, pk):
#     customer = Customer.objects.get(id=pk)
#     form = CustomerForm(instance=customer)
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('customer:customer_list')
#     ctx = {'form': form}
#     return render(request, 'customer/customer_edit.html', ctx)
#
#
# def cuDelete(request, pk):
#     customer = Customer.objects.get(id=pk)
#     form = CustomerForm()
#     if request.method == 'POST':
#         customer.delete()
#         return redirect('customer:customer_list')
#     ctx = {'form': form}
#     return render(request, 'customer/customer_delete.html', ctx)
#
#
# def customerDetails(request, pk):
#     customer = Customer.objects.get(id=pk)
#     form = CustomerForm(instance=customer)
#     return render(request, "customer/customer_details.html", {'form': form})
