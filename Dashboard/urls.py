from django.contrib import admin
from django.urls import path
from Dashboard.views import DashboardHome

app_name = 'dashboard'
urlpatterns = [
    path('', DashboardHome.as_view(), name='index'),
]

