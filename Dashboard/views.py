import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.core.exceptions import ValidationError
from Invoices.models import Item, Invoice
from Data.models import Data
from Dashboard.forms import DateForm
from Dashboard.services import (
    total_invoices,get_total_tuple,
    get_date_tuple, make_pie_graph,
    make_line_graph)


class DashboardHome(View):
    template_name = 'Dashboard/index.html'

    def get(self, request):
        all_invoices = Invoice.objects.all().order_by('date')
        data = (get_date_tuple(all_invoices), get_total_tuple(all_invoices))
        make_line_graph(data)
        form = DateForm()
        ctx = {'data': data, 'form': form}

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = DateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print()
            print("Valid")
            print()
            invoices = Invoice.objects.filter(
                date__range=[request.POST['start_date'], request.POST['end_date']]
            ).order_by('date')
            data = (get_date_tuple(invoices), get_total_tuple(invoices))
            make_line_graph(data)
            ctx = {'data': data}
            return render(request, self.template_name, ctx)
        else:
            form = DateForm()
            return render(request, self.template_name, {'form': form})


class PieChart(View):
    template_name = 'Dashboard/pie.html'

    def get(self, request):
        all_invoices = Invoice.objects.all().order_by('date')
        last_six_month = Invoice.objects.filter(
            date__range=[datetime.date.today() - datetime.timedelta(weeks=24), datetime.date.today()]
        )
        total_sales = sum(get_total_tuple(all_invoices))
        last_six_month_sales = sum(get_total_tuple(last_six_month))
        data = (total_sales, Data.objects.get(pk=1).monthly_sales)
        six_month_data = (last_six_month_sales, Data.objects.get(pk=1).monthly_sales)
        make_pie_graph(data, 0)
        make_pie_graph(six_month_data, 1)
        ctx = {'sales': total_sales}

        return render(request, self.template_name, ctx)

    def post(self, request):
        pass


