from django.contrib import admin
from .models import Invoice, Item

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    fields = ['date', 'sales_channel', 'items']


class ItemAdmin(admin.ModelAdmin):
    fields = ['product', 'quantity']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)