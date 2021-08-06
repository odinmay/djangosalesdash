from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Inventory.models import Product
from Invoices.models import Item, Invoice
from Data.models import Data
import plotly.express as px
import pandas as pd


def make_line_graph(data):
    df = pd.DataFrame(data[1], data[0])
    fig = px.line(df, labels={'index': 'Date', 'value': 'Sale Amount'})
    fig.update_layout(title='Sales Performance', title_x=0.5)
    fig.write_html('Dashboard/templates/Dashboard/graph.html', full_html=False, include_plotlyjs='cdn')
    with open('Dashboard/templates/Dashboard/graph.html', 'r') as html_f:
        html = html_f.read()

    return html


def total_invoices(queryset):
    total = 0
    for invoice in queryset:
        total += invoice.total()
    return total


def get_date_tuple(queryset):
    dates = [invoice.date.strftime("%m/%d/%Y") for invoice in queryset]
    return tuple(dates)


def get_total_tuple(queryset):
    totals = [invoice.total() for invoice in queryset]
    return tuple(totals)


def make_pie_graph(data):
    percent_complete = (data[0]/data[1]) * 100
    df = pd.DataFrame({'names': ['Sales', ' '],
                       'values':  [percent_complete, 100-percent_complete]})

    fig = px.pie(df, title='Percent to Monthly Sales Goal', values='values', names='names', hole=0.5,
                 color_discrete_sequence=['red', 'rgba(0,0,0,0)']
                 )
    fig.update_layout(title_x=0.5)
    fig.data[0].textfont.color = 'white'

    fig.write_html('Dashboard/templates/Dashboard/GraphSnippets/piesales.html', full_html=False, include_plotlyjs='cdn')

    with open('Dashboard/templates/Dashboard/GraphSnippets/piesales.html', 'r') as html_f:
        html = html_f.read()

    return html

class DashboardHome(View):
    template_name = 'Dashboard/index.html'

    def get(self, request):
        all_invoices = Invoice.objects.all().order_by('date')
        data = (get_date_tuple(all_invoices), get_total_tuple(all_invoices))
        graph_html = make_line_graph(data)
        ctx = {'data': data, 'graph': graph_html}

        return render(request, self.template_name, ctx)

    def post(self, request):
        pass


class PieChart(View):
    template_name = 'Dashboard/pie.html'

    def get(self, request):
        all_invoices = Invoice.objects.all().order_by('date')
        total_sales = sum(get_total_tuple(all_invoices))
        data = (total_sales, Data.objects.get(pk=1).monthly_sales)
        make_pie_graph(data)
        ctx = {'sales': total_sales}

        return render(request, self.template_name, ctx)
