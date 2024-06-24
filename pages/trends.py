import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html

from data.data import df

# Удалим строки с аномально высокими значениями зарплаты
df = df[df[' SalaryUSD '] < df[' SalaryUSD '].quantile(0.99)]

layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Тренды"),
            html.P("Изменение зарплат по годам")
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Выберите должности:"),
            dcc.Dropdown(
                id='trends-job-filter',
                options=[{'label': job, 'value': job} for job in df['JobTitle'].unique()],
                value=df['JobTitle'].unique().tolist(),
                multi=True
            )
        ], width=6),
        dbc.Col([
            dbc.Label("Выберите страны:"),
            dcc.Dropdown(
                id='trends-country-filter',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value=df['Country'].unique().tolist(),
                multi=True
            )
        ], width=6)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Выберите период:"),
            dcc.RangeSlider(
                id='year-range-slider',
                min=df['Survey Year'].min(),
                max=df['Survey Year'].max(),
                value=[df['Survey Year'].min(), df['Survey Year'].max()],
                marks={str(year): str(year) for year in df['Survey Year'].unique()},
                step=None
            )
        ], width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='trends-line-chart', style={'width': '100%'})
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='trends-bar-chart', style={'width': '100%'})
        ], width=12)
    ])
], fluid=True)

@callback(
    [Output('trends-line-chart', 'figure'),
     Output('trends-bar-chart', 'figure')],
    [Input('trends-job-filter', 'value'),
     Input('trends-country-filter', 'value'),
     Input('year-range-slider', 'value')]
)
def update_trends_charts(selected_jobs, selected_countries, selected_years):
    filtered_df = df[(df['JobTitle'].isin(selected_jobs)) &
                     (df['Country'].isin(selected_countries)) &
                     (df['Survey Year'] >= selected_years[0]) &
                     (df['Survey Year'] <= selected_years[1])]

    aggregated_df = filtered_df.groupby(['Survey Year', 'JobTitle'], as_index=False).agg({' SalaryUSD ': 'median'})

    print("Aggregated DataFrame:")
    print(aggregated_df.head())

    line_chart = px.line(
        aggregated_df, x='Survey Year', y=' SalaryUSD ', color='JobTitle',
        labels={'Survey Year': 'Год опроса', ' SalaryUSD ':"Средняя зарплата, $", 'JobTitle':'Должность'},
        title='Изменение зарплат по годам'
    )
    line_chart.update_layout(xaxis=dict(tickmode='linear', tick0=aggregated_df['Survey Year'].min(), dtick=1))

    bar_chart = px.bar(
        aggregated_df, x='Survey Year', y=' SalaryUSD ', color='JobTitle', barmode='group',
                labels={'Survey Year': 'Год опроса', ' SalaryUSD ':"Средняя зарплата, $", 'JobTitle':'Должность'},

        title='Средняя зарплата в год, $'
    )
    bar_chart.update_layout(xaxis=dict(tickmode='linear', tick0=aggregated_df['Survey Year'].min(), dtick=1))

    return line_chart, bar_chart
