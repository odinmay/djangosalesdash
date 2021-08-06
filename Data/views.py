from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Data
from .forms import TargetDataForm


class DataHome(View):
    template_name = 'Data/target_data_home.html'
    model = Data

    def get(self, request):
        try:
            data = Data.objects.get(pk=1)
        except Data.DoesNotExist:
            data = Data.objects.create()

        form = TargetDataForm()
        ctx = {'form': form, 'data': data}
        return render(request, self.template_name, ctx)

    def post(self, request):
        try:
            data = Data.objects.get(pk=1)
        except Data.DoesNotExist:
            data = Data.objects.create()

        form = TargetDataForm(request.POST, instance=data)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/targets')

        else:
            form = TargetDataForm(instance=data)
            return render(request, self.template_name)
