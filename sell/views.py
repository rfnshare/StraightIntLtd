from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from customer.models import Customer
from .models import *
from .forms import *
# Create your views here.
from django.views import View
from django.views.generic import *
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def index(request):
    return render(request, 'sell/create_sell.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    template_name = 'sell/create_sell.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('sell:list')


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'sell/sell_list.html'


def some_view(request, pk):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    p.drawString(100, 100, "Sample")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=pk+'.pdf')
