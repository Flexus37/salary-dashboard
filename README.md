# Добро пожаловать на сайт анализа зарплат и условий работы IT-специалистов!

## Описание

Этот проект направлен на исследование факторов, влияющих на зарплаты  IT-специалистов, включая специалистов по базам данных, и визуализацию  данных для лучшего понимания рынка труда и карьерного планирования.  Здесь вы найдете анализ зарплат, тренды, корреляции, географический и  демографический анализ, а также исследование обязанностей и задач,  выполняемых IT-специалистами.

https://flexus37.pythonanywhere.com/

## Установка

Чтобы установить и запустить этот проект, вам потребуется Python версии 3.7 или выше, а также установленные следующие библиотеки:

* dash
* dash\_bootstrap\_components
* pandas
* plotly

Вы можете установить их с помощью команды: 
```bash
pip install dash dash_bootstrap_components pandas plotly
```

Затем скачайте этот репозиторий и разместите его в выбранной директории:
```bash
git clone https://github.com/Flexus37/salary-dashboard.git
```

Запустите приложение, выполнив следующую команду в директории проекта:
```bash
python app.py
```

После запуска приложения откройте веб-браузер и перейдите по адресу **http://localhost:8050**.

Если вы столкнетесь с проблемами при установке или запуске проекта, обратитесь к нам за помощью. Мы готовы помочь вам решить любые возникающие вопросы.

## Использование

Это приложение позволяет визуализировать данные о зарплатах в IT-индустрии по различным критериям, таким как страна, должность, уровень образования и опыт работы. Для начала работы с приложением вам необходимо выполнить следующие шаги:

**Открытие приложения.** Откройте файл ```app.py``` в текстовом редакторе или IDE и запустите его. Приложение будет доступно по адресу http://localhost:8050/.

**Выбор критериев визуализации.** Вы можете выбрать критерии визуализации, используя панель фильтров, которая находится сверху от графиков. Вы можете выбрать страну, должность, уровень образования и опыт работы.

**Просматривание разных графиков.** Вы можете посмотреть разные графики, выбрав их из навигационного меню слева от графиков. Доступны следующие типы графиков: *Анализ зарплат, Тренды, Гендерный анализ зарплат, Анализ баз данных и Географический анализ*

![salary_analysis](static/images/salary_analysis.jpg)
![trends](static/images/trends.jpg)
![gender_analysis](static/images/gender_analysis.jpg)
![geo_analysis](static/images/geo_analysis.jpg)
![db_analysis](static/images/db_analysis.jpg)

## Информация о данных

В этом проекте используется датасет о зарплатах в IT-индустрии, предоставленный сайтом [Stack Overflow](https://stackoverflow.com/). Датасет содержит следующую информацию:
```markdown
* Год проведения опроса (Survey Year)
* Дата и время ответа (Timestamp)
* Размер зарплаты в долларах США (SalaryUSD)
* Страна (Country)
* Почтовый индекс (PostalCode)
* Основная база данных (PrimaryDatabase)
* Количество лет работы с этой базой данных (YearsWithThisDatabase)
* Другие базы данных, с которыми респондент работал (OtherDatabases)
* Статус занятости (EmploymentStatus)
* Должность (JobTitle)
* Наличие подчиненных (ManageStaff)
* Количество лет работы на этой должности (YearsWithThisTypeOfJob)
* Количество компаний, в которых респондент работал (HowManyCompanies)
* Количество других людей в команде респондента (OtherPeopleOnYourTeam)
* Общее количество сотрудников в компании (CompanyEmployeesOverall)
* Количество серверов баз данных (DatabaseServers)
* Образование (Education)
* Наличие образования в области компьютерных наук (EducationIsComputerRelated)
* Сертификаты (Certifications)
* Количество часов работы в неделю (HoursWorkedPerWeek)
* Количество дней в неделю, когда респондент работает удаленно (TelecommuteDaysPerWeek)
* Самая новая версия базы данных в производстве (NewestVersionInProduction)
* Самая старая версия базы данных в производстве (OldestVersionInProduction)
* Население самого большого города в пределах 20 миль от места работы (PopulationOfLargestCityWithin20Miles)
* Сфера занятости (EmploymentSector)
* Поиск другой работы (LookingForAnotherJob)
* Планы на карьеру в этом году (CareerPlansThisYear)
* Пол (Gender)
* Другие обязанности (OtherJobDuties)
* Виды выполняемых задач (KindsOfTasksPerformed)
* Счетчик (Counter)
```

Датасет содержит более 50 000 записей, собранных в результате опроса, проведенного Stack Overflow в 2021 году. Все данные предоставлены в формате CSV и доступны для скачивания на сайте Stack Overflow.

## Вклад

Мы приветствуем вклад от всех пользователей! Если вы хотите внести свой вклад в этот проект, вот что вы можете сделать:

### Отправка изменений

Если вы нашли ошибку или хотите добавить новую функцию, вы можете отправить изменения в репозиторий. Вот как это сделать:

1. Создайте форк репозитория.
2. Склонируйте свой форк на локальный компьютер.
3. Сделайте необходимые изменения в коде.
4. Отправьте изменения в свой форк.
5. Откройте pull request в оригинальный репозиторий.

### Сообщение об ошибках

Если вы нашли ошибку в проекте, пожалуйста, сообщите нам об этом. Вот как это сделать:

1. Откройте новый issue в репозитории.
2. Опишите проблему и шаги для ее воспроизведения.
3. Приложите любые необходимые файлы или скриншоты.
4. Отправьте issue.

### Предложение новых функций

Если у вас есть идеи по улучшению проекта или добавлению новых функций, пожалуйста, сообщите нам об этом. Вот как это сделать:

1. Откройте новый issue в репозитории.
2. Опишите вашу идею и ее преимущества.
3. Приложите любые необходимые файлы или скриншоты.
4. Отправьте issue.

Мы будем рады рассмотреть ваши предложения и внести их в проект!

## Контакты

Если у вас есть вопросы или предложения по проекту, вы можете связаться с нами по следующим контактам:

* [Flexus37](https://github.com/Flexus37)
* [PU6ER](https://github.com/PU6ER)
* [6Natsu9](https://github.com/6Natsu9)

Мы будем рады ответить на ваши вопросы и рассмотреть ваши предложения!
