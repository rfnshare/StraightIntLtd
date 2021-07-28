from django.shortcuts import render
from django.urls import reverse_lazy
from customer.owner import *
from .filters import *
from .forms import *


# class CustomerIndexView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class CustomerCreateView(OwnerCreateView):
    form_class = CustomerCreateForm
    paginate_by = 10
    template_name = 'customer/create_customer.html'
    success_message = "%(name)s was created successfully."
    success_url = reverse_lazy("customer:customer_list")


class CustomerListView(OwnerListView):
    filterset_class = CustomerFilter
    queryset = Customer.objects.filter(is_deleted=False)
    template_name = 'customer/customer_list.html'
    paginate_by = 10


class CustomerUpdateView(OwnerUpdateView):
    model = Customer
    template_name = 'customer/customer_edit.html'
    form_class = CustomerUpdateForm
    success_message = "%(name)s was updated successfully."
    success_url = reverse_lazy("customer:customer_list")


class CustomerDeleteView(OwnerDeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer:customer_list')
    success_message = "Session %(name)s was removed successfully"


class CustomerDetailsView(OwnerDetailView):
    model = Customer
    template_name = 'customer/customer_details.html'


def CustomerLedgerView(request, pk):
    customer = Customer.objects.get(id=pk)
    ctx = {'customer': customer}
    return render(request, 'customer/customer_ledger.html', ctx)


