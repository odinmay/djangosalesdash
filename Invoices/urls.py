from django.urls import include, path
from .views import InvoiceHome, InvoiceCreate, InvoiceDetail


app_name = 'invoices'

urlpatterns = [
    path('', InvoiceHome.as_view(), name='invoice-home'),
    path('create', InvoiceCreate.as_view(), name='invoice-create'),
    path('create/<int:pk>/', InvoiceDetail.as_view(), name='invoice-detail')
]
