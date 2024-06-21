import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from pages import salary_analysis

external_stylesheets = [dbc.themes.MATERIA]
app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "padding": "2rem 1rem",
    "color": 'white',
    "background-color": "#444",
    "box-shadow": "7px 0 15px #888"
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Анализ IT-рынка", className="display-6"),
        html.Hр(),
        html.P(
            "Проект по анализу зарплат и условий работы IT-специалистов", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Главная", href="/", active="exact"),
                dbc.NavLink("Анализ зарплат", href="/salary_analysis", active="exact"),
                # Добавьте другие страницы здесь
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            [
                html.H1("Обзор"),
                html.P("Добро пожаловать на сайт анализа зарплат и условий работы IT-специалистов!"),
                html.P(
                    "Этот проект направлен на исследование факторов, влияющих на зарплаты IT-специалистов, "
                    "включая специалистов по базам данных, и визуализацию данных для лучшего понимания рынка труда "
                    "и карьерного планирования. Здесь вы найдете анализ зарплат, тренды, корреляции, "
                    "географический и демографический анализ, а также исследование обязанностей и задач, "
                    "выполняемых IT-специалистами."
                ),
                html.Hр(),
                html.H3("Содержание:"),
                html.Ul([
                    html.Li("1. Анализ зарплат"),
                    html.Li("2. Тренды"),
                    html.Li("3. Гендерное анализ зарплат"),
                    html.Li("4. Количество серверов с базами данных по годам"),
                    html.Li("5. Географический анализ")
                ]),
                html.Img(src='/static/images/изображение.png', style={'width': '100%'})
            ],
            style={'padding': '20px'}
        )
    elif pathname == "/salary_analysis":
        return salary_analysis.layout
    return html.Div(
        [
            html.H1("404: Страница не найдена", className="text-danger"),
            html.Hр(),
            html.P(f"Путь {pathname} не найден..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
    app.run_server(debug=True)
