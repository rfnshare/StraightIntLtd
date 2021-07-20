from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


# Create your views here.

def supplier_create(request):
    form = SupplierCreateForm
    if request.method == 'POST':
        form = SupplierCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier Created Successfully')
            return redirect('supplier:list')
    ctx = {
        'form': form
    }
    return render(request, 'supplier/supplier_create.html', ctx)


def supplier_list(request):
    supplier = Supplier.objects.all()
    ctx = {
        'supplier': supplier
    }
    return render(request, 'supplier/supplier_list.html', ctx)
