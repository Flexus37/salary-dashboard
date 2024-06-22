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
            html.H1("Гендерный анализ зарплат"),
            html.P("Изменение зарплат по гендеру")
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Гендер:"),
            dcc.Checklist(
                id='gender-filter',
                options=[
                    {'label': 'Мужчина', 'value': 'Male'},
                    {'label': 'Женщина', 'value': 'Female'},
                    {'label': 'Воздержался', 'value': 'Prefer not to say'}
                ],
                value=['Male', 'Female', 'Prefer not to say'],
                inline=True
            )
        ], width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Выберите период:"),
            dcc.RangeSlider(
                id='year-range-slider-gender',
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
            dcc.Graph(id='gender-line-chart', style={'width': '100%'})
        ], width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Средняя зарплата (Мужчина)", className="card-title"),
                    html.P(id="male-salary", className="card-text")
                ])
            )
        ], width=4),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Средняя зарплата (Женщина)", className="card-title"),
                    html.P(id="female-salary", className="card-text")
                ])
            )
        ], width=4),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Средняя зарплата (Воздержался)", className="card-title"),
                    html.P(id="other-salary", className="card-text")
                ])
            )
        ], width=4)
    ])
], fluid=True)

@callback(
    [Output('gender-line-chart', 'figure'),
     Output('male-salary', 'children'),
     Output('female-salary', 'children'),
     Output('other-salary', 'children')],
    [Input('gender-filter', 'value'),
     Input('year-range-slider-gender', 'value')]
)
def update_gender_charts(selected_genders, selected_years):
    filtered_df = df[(df['Gender'].isin(selected_genders)) &
                     (df['Survey Year'] >= selected_years[0]) &
                     (df['Survey Year'] <= selected_years[1])]

    aggregated_df = filtered_df.groupby(['Survey Year', 'Gender'], as_index=False).agg({' SalaryUSD ': 'mean'})

    line_chart = px.line(
        aggregated_df, x='Survey Year', y=' SalaryUSD ', color='Gender',
        title='Изменение зарплат по гендеру'
    )
    line_chart.update_layout(xaxis=dict(tickmode='linear', tick0=aggregated_df['Survey Year'].min(), dtick=1))

    male_salary = filtered_df[filtered_df['Gender'] == 'Male'][' SalaryUSD '].mean()
    female_salary = filtered_df[filtered_df['Gender'] == 'Female'][' SalaryUSD '].mean()
    other_salary = filtered_df[filtered_df['Gender'] == 'Prefer not to say'][' SalaryUSD '].mean()

    return line_chart, f"{male_salary:.2f} руб.", f"{female_salary:.2f} руб.", f"{other_salary:.2f} руб."
