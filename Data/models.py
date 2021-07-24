from django.db import models


# Create your models here.

class Data(models.Model):
    monthly_sales = models.PositiveIntegerField(default=0)
    monthly_unit_sales = models.PositiveIntegerField(default=0)

    # Add created inventory goals and ways to check each new product added

    # monthly net sales goal
    #     weekly , daily can be inferred
    #
    # monthly units sold
    #     infer weekly unit sales
