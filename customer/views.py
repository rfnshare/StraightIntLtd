from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django_filters.views import FilterView

from .filters import *
from .forms import *


# class CustomerIndexView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerCreateForm
    paginate_by = 10
    template_name = 'customer/create_customer.html'
    success_message = "%(name)s was created successfully."
    success_url = reverse_lazy("customer:customer_list")

    def form_valid(self, form):
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message, extra_tags='text-success')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    # def get_success_url(self, **kwargs):
    #     # obj = form.instance or self.object
    #     return reverse("customer:customer_details", kwargs={'pk': self.object.pk})


class CustomerListView(LoginRequiredMixin, FilterView):
    filterset_class = CustomerFilter
    queryset = Customer.objects.filter(is_deleted=False)
    template_name = 'customer/customer_list.html'
    paginate_by = 10


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'customer/customer_edit.html'
    form_class = CustomerUpdateForm
    success_message = "%(name)s was updated successfully."
    success_url = reverse_lazy("customer:customer_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = CustomerUpdateImageForm
        return context

    def form_valid(self, form):
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message, extra_tags='text-info')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    # def get_success_url(self, **kwargs):
    #     # obj = form.instance or self.object
    #     return reverse("customer:customer_details", kwargs={'pk': self.object.pk})


class CustomerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer:customer_list')
    success_message = "Session %(name)s was removed successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__, extra_tags='text-danger')
        return super(CustomerDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, self.template_name, {'object' : customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.is_deleted = True
        customer.save()
        messages.success(request, self.success_message)
        return redirect('customer:customer_list')


class CustomerDetailsView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer/customer_details.html'


def CustomerLedgerView(request, pk):
    customer = Customer.objects.get(id=pk)
    ctx = {'customer': customer}
    return render(request, 'customer/customer_ledger.html', ctx)

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
