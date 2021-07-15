from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal(0.00))
    sale_price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name + ' x' + str(self.quantity)

    class Meta:
        verbose_name = 'Item'


class Invoice(models.Model):
    date = models.DateTimeField()
    sales_channel = models.CharField(max_length=200)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return 'Invoice #' + str(self.pk)

    class Meta:
        verbose_name = 'Invoice'

    def total(self):
        pass
