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

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD sh -c "\
    sleep 10 && \
    if python3 manage.py migrate --check --noinput; then \
        echo 'Миграции уже применены.'; \
    else \
        echo 'Применяем миграции...'; \
        python3 manage.py migrate --noinput; \
    fi && \
    echo 'Создаем суперпользователя...' && \
    python3 create_superuser.py && \
    echo 'Запуск сервера...' && \
    exec python3 manage.py runserver 0.0.0.0:8000"
