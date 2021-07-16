from django.forms import *
from Invoices.models import Invoice,Item
from Inventory.models import Product

class InvoiceForm(ModelForm):

    class Meta:
        model = Invoice
        fields = ['date', 'sales_channel']


    date = DateInput()
    sales_channel = CharField(max_length=200)
    items = ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=CheckboxSelectMultiple,
    )