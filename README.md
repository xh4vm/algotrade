# Хакатон GOALGO
[![Python version](https://img.shields.io/badge/python-v3.11-informational)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/fastapi-v0.104.1-informational)](https://fastapi.tiangolo.com/)
[![Spark verions](https://img.shields.io/badge/spark-v3.5.0-informational)](https://spark.apache.org/)
[![Clickhouse](https://img.shields.io/badge/clickhouse-v23.10.5.20-informational)](https://clickhouse.com/)
[![Airflow](https://img.shields.io/badge/airflow-v2.7.3-informational)](https://airflow.apache.org/)
[![Hadoop](https://img.shields.io/badge/hadoop-v2.0.0-informational)](https://hadoop.apache.org/)
[![Nginx](https://img.shields.io/badge/nginx-v1.25.3-informational)](https://nginx.org/ru/)
[![PostgreSQL](https://img.shields.io/badge/postgres-v16.1-informational)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/redis-v7.2.2-informational)](https://redis.io/)


## Описание
Алгоритм машинного обучения использует разные модели, чтобы предсказывать цены акций, а также обрабатывает исторические данные, чтобы выявить сложные паттерны на рынке. Важной особенностью является использование комбинации различных моделей для улучшения предсказаний и снижения рисков. Веб-сервис для инвесторов на основе этого алгоритма предоставляет удобный доступ к прогнозам, анализу рынка и визуализации результатов. Также система регулярно обновляется, чтобы быть актуальной и адаптироваться к изменяющимся условиям рынка.


## Цель работы
1. Разработать систему для оптимизации работы инвесторов/трейдеров
2. Разработать торговый алгоритм

## Задачи
- периодическая выгрузка данных algopack;
- предсказание цены актива на некоторый момент времени;
- отображение графика на некоторый временной диапазон;
- отображение графика предсказанных значений в конкретный временной диапазон;
- проведение бэктеста предсказательных алгоритмов.

## Архитектура
![goalgo-arch](https://github.com/xh4vm/algotrade/assets/87658711/944a458a-9465-46c1-9b73-d446a915225f)


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
```

## Ресурсы
- [web](http://localhost/)
- [airflow](http://localhost/airflow)
- [notebook](http://localhost/notebook) - пароль N0t3b00l

> После запуска проекта для интеграции *spark* в *airflow* не обходимо добавить Connection типа spark с параметрами: 
> - host: spark-master
> - name: spark_default
> - port: 7077
