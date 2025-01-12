1) Создать файл .env и протавить в нём следующие значения:
```bash
NAME=lms_db
HOST=postgres
PORT=5432
USER=admin
PASSWORD=admin
```
2) Запустить сервисы с помощью docker-compose:
```bash
docker-compose up -d
```