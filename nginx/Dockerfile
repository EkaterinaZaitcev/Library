# Используем официальный образ Nginx
FROM nginx:latest

# Копируем файл конфигурации Nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статические файлы веб-сайта в директорию для обслуживания
RUN mkdir -p /app/static

# Открываем порт 80 для HTTP-трафика
EXPOSE 80
