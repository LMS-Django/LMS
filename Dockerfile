FROM python:3.10-slim-buster

# Установим системные зависимости, необходимые для сборки psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Установим рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/requirements.txt

# Установим Python-зависимости
RUN python -m pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . /app

# Установка переменных окружения
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["sh", "-c", "python manage.py makemigrations main users && python manage.py migrate && python manage.py createsuperuser --noinput --first_name admin --last_name admin --email admin@example.com && python manage.py runserver 0.0.0.0:8000"]
