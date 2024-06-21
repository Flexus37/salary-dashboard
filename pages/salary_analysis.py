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
            dbc.Label("Выберите должности:"),
            dcc.Dropdown(
                id='job-filter',
                options=[{'label': job, 'value': job} for job in df['JobTitle'].unique()],
                value=df['JobTitle'].unique().tolist(),  # По умолчанию все должности
                multi=True
            )
        ], width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='pie-chart', style={'width': '100%'})
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-chart', style={'width': '100%'})
        ], width=12)
    ])
], fluid=True)

@callback(
    [Output('pie-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('job-filter', 'value')]
)
def update_charts(selected_jobs):
    filtered_df = df[df['JobTitle'].isin(selected_jobs)]
    avg_salary_df = filtered_df.groupby('JobTitle')[' SalaryUSD '].mean().reset_index()


    pie_chart = px.pie(
        avg_salary_df, names='JobTitle', values=' SalaryUSD ',
        title='Средняя зарплата по должностям'
    )

    bar_chart = px.bar(
        avg_salary_df, y='JobTitle', x=' SalaryUSD ',
        title='Средняя зарплата в год, руб',
        orientation='h'
    )

    return pie_chart, bar_chart
