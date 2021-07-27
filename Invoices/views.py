from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from Invoices.models import Item, Invoice
from django.urls import reverse_lazy
from Invoices.forms import ItemForm


class InvoiceHome(ListView):
    model = Invoice
    template_name = 'Invoices/invoice-home.html'



class InvoiceCreate(View):
    template_name = 'Invoices/invoice-create.html'
    success_url = reverse_lazy('invoices:invoice-home')

    def get(self, request):
        form = ItemForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = ItemForm(request.POST)
        ctx = {'form': form}
        print(request.POST.dict())

        if form.is_valid():

            if form.cleaned_data['invoice'] == None:
                new_invoice = Invoice.objects.create(date=request.POST['date'])
                new_invoice.save()

                item = Item.objects.create(
                    product=form.cleaned_data['product'],
                    invoice=new_invoice,
                    quantity=form.cleaned_data['quantity'],
                    sales_channel=form.cleaned_data['sales_channel'],
                )

                new_invoice.save()
                item.save()
            else:
                item = Item.objects.create(
                    product=form.cleaned_data['product'],
                    invoice=form.cleaned_data['invoice'],
                    quantity=form.cleaned_data['quantity'],
                    sales_channel=form.cleaned_data['sales_channel'],
                )
                form.cleaned_data['invoice'].date = request.POST['date']
                item.save()

            return HttpResponseRedirect('/invoices')

        else:
            form = ItemForm()
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



