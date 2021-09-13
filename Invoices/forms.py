from django import forms
from django.forms import ModelForm
from Invoices.models import Invoice, Item

from Inventory.models import Product


class InvoiceForm(forms.Form):
    date = forms.DateField()




class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



    # product = models.ModelChoiceField(Product.objects.all())
    # invoice = models.ModelChoiceField(Invoice.objects.all())

