from django.urls import include,path
from .views import ProductHome,DetailProduct, CreateProduct

app_name = 'inventory'

urlpatterns = [
    path('', ProductHome.as_view(), name='productlist'),
    path('<int:pk>/', DetailProduct.as_view(), name='productdetail'),
    path('create', CreateProduct.as_view(), name = 'productcreate'),
]