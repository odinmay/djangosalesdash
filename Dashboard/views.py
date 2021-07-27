from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Inventory.models import Product
from Invoices.models import Item, Invoice
import plotly.express as px
import pandas as pd


def make_graph(data):
    df = pd.DataFrame(data[1], data[0])
    fig = px.line(df, title='Sales Performance', labels={'index': 'Date', 'value': 'Sale Amount'})
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


class DashboardHome(View):
    template_name = 'Dashboard/index.html'

    def get(self, request):
        all_invoices = Invoice.objects.all().order_by('date')
        data = (get_date_tuple(all_invoices), get_total_tuple(all_invoices))
        graph_html = make_graph(data)
        ctx = {'data': data, 'graph': graph_html}

        return render(request, self.template_name, ctx)

    def post(self, request):
        pass
