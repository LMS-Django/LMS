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

# Копируем остальной код
COPY . /app

# Открываем порт
EXPOSE 8000

# Выполняем команды с задержкой 5 секунд
CMD ["sh", "-c", "sleep 5 && python manage.py migrate && python manage.py createsuperuser --noinput --first_name admin --last_name admin --email admin@example.com && python manage.py runserver 0.0.0.0:8000"]