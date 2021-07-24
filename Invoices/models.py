from django.db import models
from Inventory.models import Product


class Invoice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='proditem', through='Item')

    def __str__(self):
        return 'Invoice #' + str(self.pk)

    def total(self):
        total = 0
        for thing in self.item_set.all():
            total += thing.total()
        return total

    class Meta:
        verbose_name = 'Invoice'


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    sales_channel = models.CharField(max_length=100, default='Generic Sale')

    def __str__(self):
        return self.product.name

    def total(self):
        return self.quantity * self.product.sale_price

    class Meta:
        verbose_name = 'Item'
