from django.urls import include, path
from .views import InvoiceHome, InvoiceCreate, InvoiceDetail, InvoiceDelete


app_name = 'invoices'

urlpatterns = [
    path('', InvoiceHome.as_view(), name='invoice-home'),
    path('create', InvoiceCreate.as_view(), name='invoice-create'),
    path('<int:pk>/', InvoiceDetail.as_view(), name='invoice-detail'),
    path('<int:pk>/delete', InvoiceDelete.as_view(), name='invoice-delete'),
]




