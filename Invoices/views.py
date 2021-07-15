from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from Invoices.models import Item, Invoice
from django.urls import reverse_lazy


class InvoiceHome(ListView):
    model = Invoice
    template_name = 'Invoices/invoice-home.html'



class InvoiceCreate(CreateView):
    model = Invoice
    template_name = 'Invoices/invoice-create.html'
    fields = '__all__'
    success_url = reverse_lazy('invoices:invoice-home')
