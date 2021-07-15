from django.urls import include, path
from .views import InvoiceHome


app_name = 'invoices'

urlpatterns = [
    path('', InvoiceHome.as_view(), name='invoice-home'),
]
