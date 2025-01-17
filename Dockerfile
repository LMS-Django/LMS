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

# Открываем порт
EXPOSE 8000

# Скрипт запуска
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
