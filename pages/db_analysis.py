import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html

from data.data import df

df['DatabaseWorkedWith'] = df['PrimaryDatabase']
df['DatabaseCount'] = pd.to_numeric(df['DatabaseServers'], errors='coerce')

# Разметка страницы
layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("Анализ баз данных"),
            html.P("Основная используемая БД в компании"),
        ], style={'textAlign': 'center'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Период:"),
            dcc.RangeSlider(
                id='year-range-slider-db',
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
            dcc.Graph(id='database-pie-chart', style={'width': '100%', 'height': '500px'}),
        ], width=12),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='database-line-chart', style={'width': '100%', 'height': '500px'}),
        ], width=12),
    ]),
], fluid=True)

@callback(
    [Output('database-pie-chart', 'figure'),
     Output('database-line-chart', 'figure')],
    [Input('year-range-slider-db', 'value')]
)
def update_db_analysis(selected_years):
    filtered_df = df[(df['Survey Year'] >= selected_years[0]) &
                     (df['Survey Year'] <= selected_years[1])]

    db_counts = filtered_df['DatabaseWorkedWith'].value_counts().reset_index()
    db_counts.columns = ['Database', 'Count']

    pie_chart = px.pie(db_counts, values='Count', names='Database', title='Основная используемая БД в компании')
    pie_chart.update_traces(textposition='inside', textinfo='percent+label')
    pie_chart.update_layout(title_text='Основная используемая БД в компании', title_x=0.5)

    db_count_by_year = filtered_df.groupby('Survey Year')['DatabaseCount'].sum().reset_index()
    line_chart = px.line(db_count_by_year, x='Survey Year', y='DatabaseCount', title='Количество серверов с БД по годам')
    line_chart.update_layout(xaxis_title='Год опроса', yaxis_title='Количество серверов', title_x=0.5)

    return pie_chart, line_chart