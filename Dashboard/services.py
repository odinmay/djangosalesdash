import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def total_invoices(queryset):
    total = 0
    for invoice in queryset:
        total += invoice.total()
    return total


def get_date_tuple(queryset):
    try:
        dates = [invoice.date.strftime("%m/%d/%Y") for invoice in queryset]
        return tuple(dates)
    except AttributeError as e:
        print(f'Exception: {e}')



def get_total_tuple(queryset):
    totals = [invoice.total() for invoice in queryset]
    return tuple(totals)


def make_line_graph(data):
    df = pd.DataFrame(data[1], data[0])
    fig = px.line(df, labels={'index': 'Date', 'value': 'Sale Amount'})
    fig.update_layout(title='Sales Performance', title_x=0.5)
    fig.write_html('Dashboard/templates/Dashboard/GraphSnippets/graph.html', full_html=False, include_plotlyjs='cdn')
    with open('Dashboard/templates/Dashboard/GraphSnippets/graph.html', 'r') as html_f:
        html = html_f.read()
    return html


def model_query(start_date, end_date):
    # take date_ranges and query the model database
    # return model queryset
    pass


def make_pie_graph(data, num):
    percent_complete = round((data[0] / data[1]) * 100)

    labels = ['Sales', 'Goal Remaining']
    values = [percent_complete, 100 - percent_complete]
    colors = ['green', 'lightgray']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    if num == 1:
        fig.update_traces(title='Six Month Sales', sort=False, marker=dict(colors=colors), hole=0.35, hoverinfo='label',
                          textfont_size=16)

    else:
        fig.update_traces(title='Monthly Sales', sort=False, marker=dict(colors=colors), hole=0.35, hoverinfo='label',
                          textfont_size=16)

    fig.write_html(f'Dashboard/templates/Dashboard/GraphSnippets/piesales{str(num)}.html', full_html=False,
                   include_plotlyjs='cdn')

    with open(f'Dashboard/templates/Dashboard/GraphSnippets/piesales{str(num)}.html', 'r') as html_f:
        html = html_f.read()

    return html
