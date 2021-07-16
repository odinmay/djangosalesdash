from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from Invoices.models import Item, Invoice
from django.urls import reverse_lazy
from Invoices.forms import InvoiceForm


class InvoiceHome(ListView):
    model = Invoice
    template_name = 'Invoices/invoice-home.html'



class InvoiceCreate(View):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'Invoices/invoice-create.html'
    success_url = reverse_lazy('invoices:invoice-home')

    def get(self, request):
        form = InvoiceForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = InvoiceForm(request.POST)
        ctx = {'form': form}

        if form.is_valid():

            form.save()
            # new_invoice = Invoice.objects.create(
            #     date=form.cleaned_data['date'],
            #     sales_channel=form.cleaned_data['sales_channel'],
            #     item = form.cleaned_data['items'],
            # )
            return HttpResponseRedirect('/invoices')

        else:
            form = InvoiceForm()
        return render(request, self.template_name, ctx)


class InvoiceDetail(DetailView):
    model = Invoice
    template_name = 'Invoices/invoice-detail.html'
