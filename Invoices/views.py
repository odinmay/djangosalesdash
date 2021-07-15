from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from Inventory.models import Product,Item,Invoice

class InvoiceHome(View):
    model = Invoice
    template_name = 'Invoices/invoice-home.html'

    def get(self, request):
        return render(request, self.template_name)

