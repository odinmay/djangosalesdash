from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from Invoices.models import Item, Invoice
from Inventory.models import Product
from django.urls import reverse_lazy
from Invoices.forms import ItemForm, InvoiceForm
from django.forms import inlineformset_factory


class InvoiceHome(ListView):
    model = Invoice
    template_name = 'Invoices/invoice-home.html'



class InvoiceCreate(View):
    template_name = 'Invoices/invoice-create.html'
    success_url = reverse_lazy('invoices:invoice-home')
    InvoiceFormSet = inlineformset_factory(Invoice, Item, fields=('product', 'quantity'), extra=5)

    def get(self, request):
        formset = self.InvoiceFormSet()
        ctx = {'formset': formset}
        return render(request, self.template_name, ctx)

    def post(self, request):
        formset = self.InvoiceFormSet(request.POST)
        ctx = {'formset': formset}
        print(request.POST.keys())
        # if formset.is_valid():
        #     new_invoice = Invoice.objects.create(date=request.POST['date'])
        #     new_invoice.save(commit=False)
        # else:
        #     print(formset.errors)
        #
        #         new_invoice.save()
        #         item.save()
        #     else:
        #         item = Item.objects.create(
        #             product=form.cleaned_data['product'],
        #             invoice=form.cleaned_data['invoice'],
        #             quantity=form.cleaned_data['quantity'],
        #             sales_channel=form.cleaned_data['sales_channel'],
        #         )
        #         form.cleaned_data['invoice'].date = request.POST['date']
        #         item.save()
        #
        #     return HttpResponseRedirect('/invoices')

        # else:
        #     form = ItemForm()
        return render(request, self.template_name, ctx)


class InvoiceDetail(View):
    template_name = 'Invoices/invoice-detail.html'

    def get(self, request, pk):
        invoice = Invoice.objects.get(pk=pk)
        ctx = {'invoice': invoice}
        # for item in zipped_ctx:
        #     print(item)
        return render(request, self.template_name, ctx)


class InvoiceDelete(DeleteView):
    model = Invoice
    template_name = 'Invoices/invoice-delete.html'
    success_url = reverse_lazy('invoices:invoice-home')



