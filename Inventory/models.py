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

