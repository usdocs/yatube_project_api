# Проект «API для социальной сети»
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=5fe620)](https://www.djangoproject.com/)

### Краткое описание:
API для социальной сети, в которой пользователи могут публиковать записи/сообщения и просматривать сообщению других пользователей. Реализованы механизм комментариев к записям, возможность подписки на публикации интересующий авторов.
Для аутентификации используется JWT-токен.

### Стек технологий:
- Python 3.9.10
- Django 3.2.16
- Django REST Framework 3.12.4
- Simple-JWT 4.7.2

### API для сервиса __Yatube__ позволяет:
* работать с публикациями:
  * получать список всех публикаций
  * создавать (обновлять, удалять) публикации

* работать с комментариями к публикациям:
  * добавлять (получать, обновлять, удалять) комментарии

* Получать список сообществ
* Подписываться на пользователей
* Получать и обновлять JWT-токены

Ознакомиться с полным функционалом и примерами можно по эндпоинту /redoc.   

### Как запустить проект (на Windows):

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:usdocs/yatube_project_api.git 
cd yatube_project_api
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Перейти в каталог с manage.py
```bash
cd yatube_api
```

Выполнить миграции:
```bash
python manage.py migrate
```

Запустить проект:
```bash
python manage.py runserver
```

### Примеры запросов к API:
API проекта возвращает ответы в формате JSON.

##### 1. Работа с постами

- Получить список всех публикаций (возможно использование пользовательской 
пагинации):
```bash
GET /api/v1/posts/
GET /api/v1/posts/?offset=2&limit=5/
```

- Получить публикацию по id (где id=1):
```bash
GET /api/v1/posts/1/
```

- Добавление новой публикации ("text" - обязательное поле):
**анонимные запросы запрещены*
```bash
POST /api/v1/posts
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

- Обновление публикации ("text" - обязательное поле) по id (где id=1):
**только для автора публикации*
```bash
PUT /api/v1/posts/1/
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

- Частичное обновление публикации (PATCH) работает аналогично.

- Удаление публикации по id (где id=1):
**только для автора публикации*
```bash
DELETE /api/posts/1/
```

##### 2. Работа с комментариями
- Получение всех комментариев к публикации (где post_id=2):
```bash
GET /api/v1/posts/2/comments/
```

- Получение комментария к публикации по id (где post_id=2, id=1):
```bash
GET /api/v1/posts/2/comments/1/
```

- Добавление нового комментария ("text" - обязательное поле) к публикации 
(где post_id=2):
**анонимные запросы запрещены*
```bash
POST /api/v1/posts/2/comments/
{
    "text": "string"
}
```

- Обновление комментария ("text" - обязательное поле) к публикации по id 
(где post_id=2, id=1):
**только для автора публикации*
```bash
PUT /api/v1/posts/2/comments/1/
{
    "text": "string"
}
```

- Частичное обновление комментария (PATCH) работает аналогично.

- Удаление комментария к публикации по id (где post_id=2, id=1):
**только для автора публикации*
```bash
DELETE /api/v1/posts/2/comments/1/
```

##### 3. Работа с группами
- Получение списка доступных сообществ:
```bash
GET /api/v1/groups/
```

- Получение информации о сообществе по id (где id=1):
```bash
GET /api/v1/groups/1/
```

##### 4. Работа с подписками:
- Получение всех подписок пользователя, сделавшего запрос (возможен поиск по 
подпискам по параметру search):
*анонимные запросы запрещены*
```bash
GET /api/v1/follow/
GET /api/v1/follow/?search=admin
```

- Подписка пользователя, от имени которого сделан запрос на пользователя, 
переданного в теле запроса:
*анонимные запросы запрещены*
```bash
POST /api/v1/follow/
{
    "following": "string"
}
```

##### 5. Работа с токенами
- Получение JWT-токена:
```bash
POST /api/v1/jwt/create/
{
    "username": "string",
    "password": "string"
}
```

- Обновление JWT-токена:
```bash
POST /api/v1/jwt/refresh/
{
    "refresh": "string"
}
```

- Проверка JWT-токена:
```bash
POST /api/v1/jwt/verify/
{
    "token": "string"
}
```

### Разработчик проекта

Автор: Andrey Balakin  
E-mail: [usdocs@ya.ru](mailto:usdocs@ya.ru)
