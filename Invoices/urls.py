from django.urls import include, path
from .views import InvoiceHome, InvoiceCreate


app_name = 'invoices'

urlpatterns = [
    path('', InvoiceHome.as_view(), name='invoice-home'),
    path('create', InvoiceCreate.as_view(), name='invoice-create'),
]
