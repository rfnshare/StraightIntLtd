from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView


class OwnerListView(FilterView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message, extra_tags='text-success')
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        super(OwnerCreateView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def form_valid(self, form):
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.warning(self.request, success_message, extra_tags='text-info')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.error(self.request, self.success_message % obj.__dict__, extra_tags='text-danger')
        return super(OwnerDeleteView, self).delete(request, *args, **kwargs)

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview

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