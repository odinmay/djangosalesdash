from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Data
from .forms import TargetDataForm


# Create your views here.

class DataHome(View):
    template_name = 'Data/target_data_home.html'
    model = Data

    def get(self, request):
        form = TargetDataForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = TargetDataForm(request.POST)

        if form.is_valid():
            data = Data.objects.create(
                monthly_sales=form.cleaned_data['monthly_sales'],
                monthly_unit_sales=form.cleaned_data['monthly_unit_sales'],
            )

            data.save()

        return HttpResponseRedirect('/targets')
