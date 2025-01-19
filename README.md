# Платформа LMS
Участники команды:
- Шарнин Никита Сергеевич
- Шандрюк Пётр Николаевич

# Оглавление
1. [Постановка задачи](#постановка-задачи)
2. [Развертывание](#развертывание)

# Постановка задачи

Создание курсов администратором системы, назначения преподавателя на курс. Преподаватель формирует группы из пользователей, отмечает посещаемость, открывае>
Выбрать любую из представленных задач для решения, подойти творчески к решению задачи, в описании лишь базовый функционал написан, нужно продумать детали. >
# Развёртывание

1) Создать файл .env и проставить в нём следующие значения:
```bash
NAME=lms_db
HOST=postgres
PORT=5432
USER=admin
PASSWORD=admin
IP={публичный ip адрес вашей виртуальной машины}
```
2) Запустить сервисы с помощью docker-compose:
```bash
docker-compose up -d
```

3) Вписать в файле lms/settings.py публичный ip-адрес виртуальной машины
```py
ALLOWED_HOSTS = ['{публичный ip адрес вашей виртуальной машины}']
```

4) Выдать файлу entrypoint.sh права на исполнение
```bash
sudo chmod +x entrypoint.sh
```

После этих действий и успешного запуска контейнеров можно с помощью браузера переходить на сайт через порт 8000

# Структура проекта

├── Dockerfile
├── README.md
├── create_superuser.py
├── docker-compose.yaml
├── entrypoint.sh
├── get-docker.sh
├── lms
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── main
│   │       ├── 404.html
│   │       ├── all_courses_list.html
│   │       ├── base.html
│   │       ├── course_details.html
│   │       ├── login_page.html
│   │       ├── logout.html
│   │       ├── main.html
│   │       ├── profile.html
│   │       └── register_page.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── project_structure.txt
├── requirements.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   └── users
    │       ├── base.html
    │       ├── login_page.html
    │       ├── logout.html
    │       ├── profile.html
    │       └── register_page.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
