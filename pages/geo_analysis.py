import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html

from data.data import df

# Удалим строки с аномально высокими значениями зарплаты
df = df[df[' SalaryUSD '] < df[' SalaryUSD '].quantile(0.99)]

# Добавим дополнительные параметры для анализа
df['Experience'] = pd.to_numeric(df['YearsWithThisTypeOfJob'], errors='coerce')
df['CompanySize'] = pd.to_numeric(df['CompanyEmployeesOverall'], errors='coerce')

# Словарь для названий параметров
parameter_names = {
    ' SalaryUSD ': 'средней зарплате',
    'Experience': 'среднему количеству опыта',
    'CompanySize': 'среднему количеству сотрудников'
}

layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Географический анализ"),
            html.P("Параметры по странам")
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='parameter-dropdown',
                options=[
                    {'label': 'Средняя зарплата', 'value': ' SalaryUSD '},
                    {'label': 'Среднее количество опыта', 'value': 'Experience'},
                    {'label': 'Среднее количество сотрудников', 'value': 'CompanySize'}
                ],
                value=' SalaryUSD ',
                clearable=False
            )
        ], width=4)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='geo-map', style={'width': '100%', 'height': '700px'})
        ], width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(
                id='year-range-slider-geo',
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
        dbc.Col([], width=4),
        dbc.Col([
            dbc.Card(dbc.CardBody([
                html.H4(id='top-countries-title', style={'textAlign': 'center'}),
                html.Div(id='top-countries-card', style={'padding': '10px'})
            ]), style={
                'padding': '15px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)'
            }),
        ], width=4),
        dbc.Col([], width=4),
    ])
], fluid=True)

@callback(
    [Output('geo-map', 'figure'),
     Output('top-countries-title', 'children'),
     Output('top-countries-card', 'children')],
    [Input('year-range-slider-geo', 'value'),
     Input('parameter-dropdown', 'value')]
)
def update_geo_analysis(selected_years, selected_parameter):
    filtered_df = df[(df['Survey Year'] >= selected_years[0]) &
                     (df['Survey Year'] <= selected_years[1])]

    avg_param_country = filtered_df.groupby('Country', as_index=False)[selected_parameter].mean()
    top_countries = avg_param_country.nlargest(5, selected_parameter)

    fig = px.choropleth(avg_param_country, locations="Country",
                        locationmode='country names', color=selected_parameter,
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        labels={'Country': 'Страна', selected_parameter: 'Значение'},
                        title='Параметры по странам')

    top_countries_title = f"ТОП-5 стран по {parameter_names[selected_parameter]}"

    suffix = "$" if selected_parameter == ' SalaryUSD ' else ""

    top_countries_card = html.Div([
        html.Div([
            html.Span(f"{country}", style={'fontWeight': 'bold', 'paddingRight': '10px'}),
            html.Span(f"{value:.2f} {suffix}", style={'fontWeight': 'bold', 'paddingLeft': '10px'})
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'padding': '10px',
            'margin': '5px 0',
            'borderRadius': '5px',
            'color': 'white',
            'backgroundColor': color
        })
        for country, value, color in zip(
            top_countries['Country'],
            top_countries[selected_parameter],
            ['#ff6f61', '#ffcc5c', '#88d8b0', '#6a9fb5', '#f29e4c']
        )
    ])

    return fig, top_countries_title, top_countries_card