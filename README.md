# Хакатон GOALGO moex

## Запуск проекта

``` 
# Копирование переменных окружения
cp .env.example .env 

# Скачать образ кликхауса
docker pull clickhouse/clickhouse-server:23.10.5.20-alpine

# Копирование файлов настроек для nginx
rm -rf ./nginx/static && cp -r ./nginx/static_defaults/ ./nginx/static

# Запуск проекта
make run
