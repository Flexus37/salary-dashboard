import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, callback, dcc, html
from data.data import df

# Удалим строки с аномально высокими значениями зарплаты
df = df[df[' SalaryUSD '] < df[' SalaryUSD '].quantile(0.99)]

# Средняя зарплата по странам
avg_salary_country = df.groupby('Country', as_index=False)[' SalaryUSD '].mean()

layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Географический анализ"),
            html.P("Средняя зарплата по странам")
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='geo-map', style={'width': '100%'})
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
                html.H4("ТОП-5 стран по ЗП", style={'textAlign': 'center'}),
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
     Output('top-countries-card', 'children')],
    [Input('year-range-slider-geo', 'value')]
)
def update_geo_analysis(selected_years):
    filtered_df = df[(df['Survey Year'] >= selected_years[0]) & 
                     (df['Survey Year'] <= selected_years[1])]
    
    avg_salary_country = filtered_df.groupby('Country', as_index=False)[' SalaryUSD '].mean()
    top_countries = avg_salary_country.nlargest(5, ' SalaryUSD ')

    fig = px.choropleth(avg_salary_country, locations="Country", 
                        locationmode='country names', color=" SalaryUSD ",
                        hover_name="Country", 
                        color_continuous_scale=px.colors.sequential.Plasma,
                        labels={'Country':'Страна', ' SalaryUSD ':'Средняя зарплата, руб'},
                        title='Средняя зарплата по странам')
    
    # top_countries_list = [html.Li(f"{country}: {salary:.2f} руб.") for country, salary in zip(top_countries['Country'], top_countries[' SalaryUSD '])]

    top_countries_card = html.Div([
        html.Div([
            html.Span(f"{country}", style={'fontWeight': 'bold', 'paddingRight': '10px'}),
            html.Span(f"{salary:.2f} руб.", style={'fontWeight': 'bold', 'paddingLeft': '10px'})
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'padding': '10px',
            'margin': '5px 0',
            'borderRadius': '5px',
            'color': 'white',
            'backgroundColor': color
        })
        for country, salary, color in zip(
            top_countries['Country'], 
            top_countries[' SalaryUSD '], 
            ['#ff6f61', '#ffcc5c', '#88d8b0', '#6a9fb5', '#f29e4c']
        )
    ])
    
    return fig, top_countries_card

if __name__ == '__main__':
    app.run_server(debug=True)
