import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html

from data.data import df



# Разметка страницы
layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("О проекте", style={"textAlign":"center"}),
            html.P(
                    "Этот проект направлен на исследование факторов, влияющих на зарплаты IT-специалистов, "
                    "включая специалистов по базам данных, и визуализацию данных для лучшего понимания рынка труда "
                    "и карьерного планирования. Здесь вы найдете анализ зарплат, тренды, корреляции, "
                    "географический и демографический анализ, а также исследование обязанностей и задач, "
                    "выполняемых IT-специалистами."
                ),
            html.A("Исходный код проекта доступен на GitHub", href="https://github.com/Flexus37/salary-dashboard"),
            html.Hr(),
           html.H2("Информация о данных", style={"textAlign":'center'}),
            html.P("В этом проекте используется датасет о зарплатах в IT-индустрии, предоставленный сайтом Stack Overflow. Датасет содержит следующую информацию:"),
            html.Pre([
                html.Code(
                    "* Год проведения опроса (Survey Year)\n"
                    "* Дата и время ответа (Timestamp)\n"
                    "* Размер зарплаты в долларах США (SalaryUSD)\n"
                    "* Страна (Country)\n"
                    "* Почтовый индекс (PostalCode)\n"
                    "* Основная база данных (PrimaryDatabase)\n"
                    "* Количество лет работы с этой базой данных (YearsWithThisDatabase)\n"
                    "* Другие базы данных, с которыми респондент работал (OtherDatabases)\n"
                    "* Статус занятости (EmploymentStatus)\n"
                    "* Должность (JobTitle)\n"
                    "* Наличие подчиненных (ManageStaff)\n"
                    "* Количество лет работы на этой должности (YearsWithThisTypeOfJob)\n"
                    "* Количество компаний, в которых респондент работал (HowManyCompanies)\n"
                    "* Количество других людей в команде респондента (OtherPeopleOnYourTeam)\n"
                    "* Общее количество сотрудников в компании (CompanyEmployeesOverall)\n"
                    "* Количество серверов баз данных (DatabaseServers)\n"
                    "* Образование (Education)\n"
                    "* Наличие образования в области компьютерных наук (EducationIsComputerRelated)\n"
                    "* Сертификаты (Certifications)\n"
                    "* Количество часов работы в неделю (HoursWorkedPerWeek)\n"
                    "* Количество дней в неделю, когда респондент работает удаленно (TelecommuteDaysPerWeek)\n"
                    "* Самая новая версия базы данных в производстве (NewestVersionInProduction)\n"
                    "* Самая старая версия базы данных в производстве (OldestVersionInProduction)\n"
                    "* Население самого большого города в пределах 20 миль от места работы (PopulationOfLargestCityWithin20Miles)\n"
                    "* Сфера занятости (EmploymentSector)\n"
                    "* Поиск другой работы (LookingForAnotherJob)\n"
                    "* Планы на карьеру в этом году (CareerPlansThisYear)\n"
                    "* Пол (Gender)\n"
                    "* Другие обязанности (OtherJobDuties)\n"
                    "* Виды выполняемых задач (KindsOfTasksPerformed)\n"
                    "* Счетчик (Counter)"
                , style={"whiteSpace": "pre-wrap", "textAlign":"start"})
            ]),
            html.P("Датасет содержит более 50 000 записей, собранных в результате опроса, проведенного Stack Overflow в 2021 году. Все данные предоставлены в формате CSV и доступны для скачивания на сайте Stack Overflow."),
            html.Hr(),
            html.H2("Контакты", style={"textAlign":'center'}),
            html.P("Если у вас есть вопросы или предложения по проекту, вы можете связаться с нами по следующим контактам:"),
            html.Ul([
                html.Li(html.A("Flexus37", href="https://github.com/Flexus37",)),
                html.Li(html.A("PU6ER", href="https://github.com/PU6ER",)),
                html.Li(html.A("6Natsu9", href="https://github.com/6Natsu9",)),

                ]),
            html.P("Мы будем рады ответить на ваши вопросы и рассмотреть ваши предложения!"),

        ], style={'textAlign': ''})
    ]),
], fluid=True)

