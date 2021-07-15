from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'cost', 'sale_price', 'stock']





admin.site.register(Product, ProductAdmin)

