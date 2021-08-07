from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.

def select_supplier(request):
    form = SelectSupplierForm
    if request.method == 'POST':
        form = SelectSupplierForm(request.POST)
        if form.is_valid():
            supplierid = request.POST.get("supplier")
            supplier = get_object_or_404(Supplier, id=supplierid)
            return redirect('purchase:create', supplier.id)
    ctx = {
        'form': form
    }
    return render(request, 'purchase/purchase.html', ctx)


def purchase_create(request, pk):
    formset = PurchaseForm(request.GET or None)  # renders an empty formset
    PurchaseForm.base_fields['products'] = forms.ModelChoiceField(queryset=Product.objects.filter(supplier_id=pk))
    supplierobj = get_object_or_404(Supplier, pk=pk)  # gets the supplier object
    if request.method == 'POST':
        formset = PurchaseForm(request.POST)  # recieves a post method for the formset
        supplierobj = get_object_or_404(Supplier, pk=pk)  # gets the supplier object
        if formset.is_valid():
            # saves bill
            # billobj = PurchaseBill(
            #     supplier=supplierobj)  # a new object of class 'PurchaseBill' is created with supplier field set to 'supplierobj'
            # billobj.save()  # saves object into the db
            # # create bill details object
            # billdetailsobj = PurchaseBillDetails(billno=billobj)
            # billdetailsobj.save()
            # for form in formset:  # for loop to save each individual form as its own object
            #     # false saves the item and links bill to the item
            #     billitem = form.save(commit=False)
            #     billitem.billno = billobj  # links the bill object to the items
            #     # gets the stock item
            #     stock = get_object_or_404(Stock, name=billitem.stock.name)  # gets the item
            #     # calculates the total price
            #     billitem.totalprice = billitem.perprice * billitem.quantity
            #     # updates quantity in stock db
            #     stock.quantity += billitem.quantity  # updates quantity
            #     # saves bill item and stock
            #     stock.save()
            #     billitem.save()
            formset.save()
            messages.success(request, "Purchased items have been registered successfully")
            return redirect('purchase:list')
    context = {
        'formset': formset,
        'supplier': supplierobj,
    }  # sends the supplier and formset as context
    return render(request, 'purchase/purchase_create.html', context)
# class PurchaseCreateView(CreateView):
#     template_name = 'purchase/purchase_create.html'
#     form_class = PurchaseForm
#     success_url = reverse_lazy('purchase:list')
#
#     def get_context_data(self, **kwargs):
#         context = super(PurchaseCreateView, self).get_context_data(**kwargs)
#         supplierobj = get_object_or_404(Supplier, pk=self.kwargs['pk'])
#         context['supplier'] = supplierobj
#         PurchaseForm.base_fields['products'] = forms.ModelChoiceField(queryset=Product.objects.filter(supplier_id=2))
#         return context


def purchase_list(request):
    purchase = Purchase.objects.all()
    ctx = {
        'purchase': purchase,
    }
    return render(request, 'purchase/purchase_list.html', ctx)
