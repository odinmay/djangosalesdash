from django.forms import ModelForm
from .models import Data


class TargetDataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['monthly_sales', 'monthly_unit_sales']
