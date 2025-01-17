#!/bin/sh

# Ждем 5 секунд, чтобы база данных была готова
sleep 5

# Проверяем и выполняем миграции только если они еще не применены
if python manage.py migrate --check --noinput; then
    echo "Миграции уже применены."
else
    echo "Применяем миграции..."
    python manage.py migrate --noinput
fi

# Создаем суперпользователя, если он не существует
echo "Создаем суперпользователя..."
python create_superuser.py

# Запускаем сервер
echo "Запуск сервера..."
exec python manage.py runserver 0.0.0.0:8000
