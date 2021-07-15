from django.contrib import admin
from .models import Product, Invoice, Item


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'cost', 'sale_price', 'stock']


class InvoiceAdmin(admin.ModelAdmin):
    fields = ['date', 'sales_channel', 'items']


class ItemAdmin(admin.ModelAdmin):
    fields = ['product', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
