# API для управления библиотекой
## Описание проекта
Проект представляет собой REST API для управления библиотекой. API позволяет работать с книгами, авторами, пользователями, а также отслеживать выдачу книг и их возврат. Проект построен на фреймворке Django с использованием Django REST Framework и JWT для аутентификации.
## Основной функционал:
- Управление книгами (создание, редактирование, удаление, поиск по различным критериям).
- Управление авторами (создание, редактирование, удаление).
- Управление пользователями (регистрация, авторизация, получение информации).
- Выдача и возврат книг пользователям.
- Аутентификация с помощью JWT (JSON Web Tokens).
## Стек технологий:
- Backend: Django, Django REST Framework
- База данных: PostgreSQL
- Аутентификация: JWT (используя djangorestframework-simplejwt)
- Контейнеризация: Docker, Docker Compose
- Документация API: OpenAPI (Swagger / ReDoc)
- Формат кода: PEP8
## Установка и запуск проекта
1. Клонирование репозитория
- ```bash
  https://github.com/EkaterinaZaitcev/Library.git
2. Установка зависимостей из файла 
- ```bash 
  pip install -r requirements.txt
3. Настройте файл окружения:
Скопируйте .env.sample в .env и настройте переменные окружения в файле .env.

4. Применение миграции:
- ```bash 
  python manage.py migrate
  
5. Для заполнения тестовой базы данных используйте команды:
- Команда для создания администратора
- ```bash 
  python manage.py csu
- Добавление данных в базу данных  
- ```bash
  python manage.py loaddata author.json
  python manage.py loaddata library.json
  python manage.py loaddata rental.json

6. Запуск сервера
- ```bash
  python manage.py runserver
  ```
  
## **Запуск проекта с Docker**

Убедитесь, что у вас установлен Docker и Docker Compose. 
Для запуска контейнеров используйте следующую команду:
- ```bash
  docker-compose up -d --build
  ```
  
## Документация доступна по адресу:

http://127.0.0.1:8000/swager/

http://127.0.0.1:8000/redoc/