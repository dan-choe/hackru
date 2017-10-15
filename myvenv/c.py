# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go


accidental = 0
non_accidental = 0

app = dash.Dash()

colors = {
    'background': '#eee',
    'text': '#000'
}


header = "default"
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='HackRU Data Visualization',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='''
        Vitech
    '''),
    dcc.Graph(
        id='example-graph1',
        figure={
            'data': [
                {'x': [accidental,non_accidental], 'y': [100, 10], 'type': 'bar', 'name': 'Dental'},
                {'x': [accidental,non_accidental], 'y': [5, 24], 'type': 'bar', 'name': 'Accidental'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    dcc.Graph(
        id='example-graph3',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [20, 23, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [92, 24, 35], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Graph(
        id='example-graph4',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [100, 23, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [92, 24, 35], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)