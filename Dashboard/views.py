from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class DashboardHome(View):
    template_name = 'Dashboard/index.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
