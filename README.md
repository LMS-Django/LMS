1) Создать виртуальное окружение (или подключить имеющееся)
2) Импортировать все необходимые библиотеки: `pip install -r requirements.txt`
3) В файле .env проставить значения, необходимые для установления соединения с postgresql
4) Выполнить миграцию: `python manage.py migrate`
5) Создать суперпользователя `python manage.py createsuperuser`
6) Запустить сервер: `python manage.py runserver`
   