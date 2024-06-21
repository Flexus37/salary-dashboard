import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Input, Output, callback, dcc, html

from data.data import df

layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Анализ зарплат"),
            html.P("Средняя зарплата по должностям")
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                figure=px.pie(
                    df, names='position', values='salary',
                    title='Средняя зарплата по должностям'
                )
            )
        ], width=6),
        dbc.Col([
            dcc.Graph(
                figure=px.bar(
                    df, x='position', y='salary',
                    title='Средняя зарплата в год, руб'
                )
            )
        ], width=6)
    ])
])
