from django.forms import *
from Invoices.models import Invoice, Item
from Inventory.models import Product


# class InvoiceForm(ModelForm):
#     class Meta:
#         model = Invoice
#         fields = '__all__'



class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



    # product = models.ModelChoiceField(Product.objects.all())
    # invoice = models.ModelChoiceField(Invoice.objects.all())

