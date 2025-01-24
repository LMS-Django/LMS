# Платформа LMS
Участники команды:
- Шарнин Никита Сергеевич
- Шандрюк Пётр Николаевич

# Оглавление
1. [Постановка задачи](#постановка-задачи)
2. [Развертывание](#развертывание)
3. [Структура проекта](#структура-проекта)

# Постановка задачи

Создание курсов администратором системы, назначения преподавателя на курс. Преподаватель формирует группы из пользователей, отмечает посещаемость, открывает и закрывает темы. Учащиеся имеют доступ только к своему курсу. Могут изучать материал курса, присылать домашнее задание, в виде файла или ссылки на облачный диск.
# Развёртывание

1) Создать файл .env и проставить в нём следующие значения:
```bash
NAME=lms_db
HOST=postgres
PORT=5432
USER=admin
PASSWORD=admin
ALLOWED_HOSTS={ip адрес вашей ВМ}
```
2) Запустить сервисы с помощью docker-compose:
```bash
docker-compose up -d
```

После этих действий и успешного запуска контейнеров можно с помощью браузера переходить на сайт через порт 8000

# Структура проекта

```plaintext 
├── Dockerfile
├── README.md
├── docker-compose.yaml
├── lms
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── exceptions.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── exceptions.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_course_students_alter_course_teacher.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_course_students_alter_course_teacher.cpython-310.pyc
│   │       ├── 0002_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── templates
│   │   └── main
│   │       ├── 404.html
│   │       ├── add_students.html
│   │       ├── add_topic.html
│   │       ├── all_courses_list.html
│   │       ├── base.html
│   │       ├── change_course.html
│   │       ├── change_task.html
│   │       ├── course_details.html
│   │       ├── delete_task.html
│   │       ├── get_task.html
│   │       ├── main.html
│   │       ├── upload_homework.html
│   │       └── upload_task.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   └── assignments
│       └── files
│           └── Резюме.pdf
├── project_structure.txt
├── requirements.txt
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   ├── admin.cpython-310.pyc
    │   ├── apps.cpython-310.pyc
    │   ├── forms.cpython-310.pyc
    │   ├── models.cpython-310.pyc
    │   ├── urls.cpython-310.pyc
    │   └── views.cpython-310.pyc
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-310.pyc
    │       └── __init__.cpython-310.pyc
    ├── models.py
    ├── templates
    │   └── users
    │       ├── base.html
    │       ├── login_page_student.html
    │       ├── login_page_teacher.html
    │       ├── logout.html
    │       ├── profile.html
    │       ├── register_page.html
    │       └── reset_password.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
