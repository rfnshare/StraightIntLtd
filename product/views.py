from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.
from django.views import View


# def index(request):
#     return render(request, 'product/create_product.html')
#
#
# class ProtectView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request, 'product/create_product.html')

def create_product_category(request):
    form = ProductCategoryCreateForm
    if request.method == 'POST':
        form = ProductCategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:create_category')
    category = ProductCategory.objects.all()
    ctx = {
        'form': form,
        'category': category
    }
    return render(request, 'product/create_product_category.html', ctx)


def create_product(request):
    form = ProductCreateForm
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Created Successfully')
            return redirect('product:list')
    ctx = {
        'form': form,
    }
    return render(request, 'product/create_product.html', ctx)


def product_list(request):
    product = Product.objects.all()
    ctx = {
        'product': product,
    }
    return render(request, 'product/product_list.html', ctx)
