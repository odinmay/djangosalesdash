from django.urls import path
from .views import DataHome

app_name = 'targetdata'

urlpatterns = [
    path('', DataHome.as_view(), name='target_data_home')
]