from django.forms import *
from Invoices.models import Invoice, Item
from Inventory.models import Product


# class InvoiceForm(ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ['date', 'sales_channel']
#
#     date = DateInput()
#     sales_channel = CharField(max_length=200)
#     items = ModelMultipleChoiceField(
#         queryset=Product.objects.all(),
#         widget=CheckboxSelectMultiple,
#     )
#     quantity = IntegerField()


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



    # product = models.ModelChoiceField(Product.objects.all())
    # invoice = models.ModelChoiceField(Invoice.objects.all())

