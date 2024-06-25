import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback, dcc, html

from data.data import df

# Обработка данных
df['Survey Year'] = df['Survey Year'].astype(int)
df[' SalaryUSD '] = pd.to_numeric(df[' SalaryUSD '], errors='coerce')

# Заполнение пропущенных значений в столбце Gender
df['Gender'] = df['Gender'].fillna('Not Asked')

# Проверка наличия данных за 2017 год после заполнения
print("Данные за 2017 год после заполнения пропущенных значений в Gender:")
print(df[df['Survey Year'] == 2017]['Gender'].value_counts())

# Создание функции для расчета средней зарплаты по гендеру и году
def calculate_average_salary(df, gender, years):
    filtered_df = df[(df['Gender'] == gender) & (df['Survey Year'].between(years[0], years[1]))]
    print(f"Filtered data for {gender} between {years[0]} and {years[1]}:\n", filtered_df['Survey Year'].value_counts())
    return filtered_df.groupby('Survey Year')[' SalaryUSD '].mean().reset_index()

# Разметка страницы
layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Гендерный анализ зарплат"),
            html.P("Анализ средней зарплаты по гендеру за выбранный период."),
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Гендер:", style={'font-size': '20px'}),
            dcc.Checklist(
                id='gender-checklist',
                options=[
                    {'label': html.Span('Мужчина', style={'fontSize': '18px', 'marginRight': '15px'}), 'value': 'Male'},
                    {'label': html.Span('Женщина', style={'fontSize': '18px', 'marginRight': '15px'}), 'value': 'Female'},
                    {'label': html.Span('Воздержался', style={'fontSize': '18px', 'marginRight': '15px'}), 'value': 'Prefer not to say'},
                    {'label': html.Span('Неизвестно', style={'fontSize': '18px', 'marginRight': '15px'}), 'value': 'Not Asked'}
                ],
                value=['Male', 'Female', 'Prefer not to say', 'Not Asked'],
                inline=True,
                style={'font-size': '18px', 'display': 'flex', 'flex-wrap': 'wrap'}
            ),
        ], width=12),
    ], style={'margin-bottom': '20px'}),
    dbc.Row([
        dbc.Col([
            dbc.Label("Период:", style={'font-size': '20px'}),
            dcc.RangeSlider(
                id='year-slider',
                min=df['Survey Year'].min(),
                max=df['Survey Year'].max(),
                step=1,
                value=[df['Survey Year'].min(), df['Survey Year'].max()],
                marks={str(year): str(year) for year in df['Survey Year'].unique()}
            ),
        ], width=12),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='salary-graph', style={'width': '100%', 'height': '500px'}),
        ], width=12),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div(id='average-salary-indicators', style={'margin-top': '20px', 'display': 'flex', 'justify-content': 'space-around'})
        ], width=12),
    ]),
], fluid=True)

@callback(
    [Output('salary-graph', 'figure'),
     Output('average-salary-indicators', 'children')],
    [Input('gender-checklist', 'value'),
     Input('year-slider', 'value')]
)
def update_graph(selected_genders, selected_years):
    print(f"Selected years: {selected_years}")
    traces = []
    indicators = []
    translated_gender = {
        'Male': 'Мужчина',
        'Female': 'Женщина',
        'Prefer not to say': 'Воздержался',
        'Not Asked': 'Неизвестно'
    }
    for gender in selected_genders:
        average_salary_df = calculate_average_salary(df, gender, selected_years)
        if not average_salary_df.empty:
            trace = go.Scatter(
                x=average_salary_df['Survey Year'],
                y=average_salary_df[' SalaryUSD '],
                mode='lines+markers',
                name=f'{translated_gender.get(gender, gender)}'
            )
            traces.append(trace)

            # Расчет средней зарплаты за весь выбранный период
            overall_avg_salary = average_salary_df[' SalaryUSD '].mean()
            indicators.append(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5(f" ({translated_gender.get(gender, gender)}):", className="card-title"),
                            html.P(f"{overall_avg_salary:.2f} USD", className="card-text"),
                        ]
                    ),
                    style={"width": "18rem"},
                )
            )

    figure = {
        'data': traces,
        'layout': go.Layout(
            title='Гендерный анализ зарплат',
            xaxis={'title': 'Год', 'dtick': 1},
            yaxis={'title': 'Средняя зарплата (USD)'},
            hovermode='closest',
            legend={'title': 'Гендер'}
        )
    }
    return figure, indicators
