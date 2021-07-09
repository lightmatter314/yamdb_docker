## Проект YaMDb (RESTful API) - база отзывов о фильмах, книгах и музыке.
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title).

## Установка

#### 1. Установить docker и docker_compose
```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
apt install docker_compose
```

#### 2. Склонировать репозиторий  
```git clone https://github.com/lightmatter314/infra_sp2.git```

#### 3. Создать .ENV файл по шаблону 
```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=p&l%385148kslh3451^##a1)ilz@4zqj=rq&agdol^##zgl9(vs # Секретный ключ
```

#### 4. Создать образ и запуск контейнера
```docker-compose up --build -d```

#### 5. Подготовить и сделать миграции 
```
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
```

#### 6. Создать суперпользователя
```docker-compose exec web python manage.py createsuperuser```

#### 7. Загрузить статику для nginx:
```docker-compose exec web python manage.py collectstatic --no-input```

### Дополнительные возможности:
#### Заполнить БД тестовыми данными:
```docker-compose exec web python3 manage.py loaddata fixtures.json```
#### Пример бэкапа/дампа данных
```docker-compose exec web python manage.py dumpdata > fixtures.json```
#### Тестирование целостности проекта
```docker-compose exec web pytest```

### Стек технологий
- Python 3.8.5
- Django 3.0.5
- Django Rest Framework 3.11.0
- Docker 20.10.6
- docker-compose 1.25.0
- gunicorn 20.0.4
- Nginx 1.19.3
- Postgres 12.4


### Документация доступна по адресу: 
https://localhost:8000/redoc
### Администрирование доступно по адресу: 
https://localhost:8000/admin/

### Алгоритм регистрации пользователей
- Пользователь отправляет запрос с параметром email на /auth/email/.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
- Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).
- При желании пользователь отправляет PATCH-запрос на /users/me/ и заполняет поля в своём профайле (описание полей — в документации).

