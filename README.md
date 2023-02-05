![](https://img.shields.io/badge/Python-3.7.5-blue)
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
![](https://img.shields.io/badge/Docker-3.8-yellow)
![example workflow](https://github.com/oitczvovich/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
<br><br>
# YaMDb


## Описание
Проект YaMDb собирает отзывы пользователей на произведения.
Возможности:
▪️ Регистрация на сайте, получение токена, изменение данных своей учетной записи
▪️ Раздаление прав пользователей согласно, назначенной ему роли
▪️ Возможность, согласно авторизации выполнять следующие дествия: получать, добавлять и удалять - категорию, жанр, произведение, отзыв и комментарий
▪️ Администрирование пользователями

## Технологии в проекте<br>
🔹 Python<br>
🔹 Django<br>
🔹 Django REST Framework<br>
🔹 Docker<br>

## Развернуть локально
1. Склонировать репозиторий через консоль:
```bash
git clone https://github.com/oitczvovich/infra_sp2
```
2. Создать .env файл внутри директории infra (на одном уровне с docker-compose.yaml) Пример .env файла:
```bash
SECRET_KEY = 'Ваш ключ'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
3. Запуск тестов (опционально, если не нужно - переходите к следующему шагу) Создать и активировать виртуальное пространство, установить зависимости.<br>

-Для Windows:
```bash
cd infra_sp2
python -m venv venv
source venv/Scripts/activate
cd api_yamdb
pip install -r requirements.txt
cd ..
pytest
```
-Для Mac/Linux:
```bash
cd infra_sp2
python3 -m venv venv
source venv/bin/activate
cd api_yamdb
pip install -r requirements.txt
cd ..
pytest
```
4. Запуск Docker контейнеров: Убедиться, что Docker установлен и готов к работе
```bash
docker --version
```
Запустите docker-compose
```bash
cd infra/
docker-compose up -d --build
```
5. Выполните миграции, создайте суперпользователя и перенесите статику:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
6. Наполните базу данных тестовыми данными:
```bash
docker cp fixtures.json infra-web-1:/app
docker exec infra-web-1 python manage.py loaddata fixtures.json
```
7. Проверьте доступность сервиса
http://localhost/admin<br>

### Документация
http://localhost/redoc/

## Авторы проекта
### Скалацкий Владимир
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovi
