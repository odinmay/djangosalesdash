from django.contrib import admin
from .models import Invoice, Item

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    fields = ['invoice', 'product', 'quantity', 'sales_channel']


admin.site.register(Invoice)
admin.site.register(Item, ItemAdmin)
