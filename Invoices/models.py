from django.db import models
from Inventory.models import Product


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
