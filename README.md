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
Торговый алгоритм, основанный на машинном обучении, представляет собой инновационный подход к анализу и прогнозированию цен акций. Используя разнообразие моделей, таких как Time Series Forecasting, XGBoost и Random Forest, алгоритм стремится обеспечить более точное и стабильное предсказание динамики рынка.

На начальном этапе работы алгоритм осуществляет загрузку и предварительную обработку исторических данных, включая технические индикаторы, объем торгов и предыдущие значения цен. Обучение моделей проводится на обширном временном ряде, что позволяет алгоритму выявлять сложные паттерны и тренды в динамике рынка.

Одной из ключевых особенностей алгоритма является использование ансамблей, таких как Voting Ensemble. Это позволяет совмещать прогнозы различных моделей, улучшая обобщающую способность и повышая устойчивость предсказаний. Ансамбли также помогают справляться с потенциальными слабостями отдельных моделей.

Веб-сервис для инвесторов, построенный на основе данного алгоритма, предоставляет удобный интерфейс для получения предсказаний цен акций, аналитики рынка и визуализации результатов. Ключевые метрики, такие как MAE, MSE, R^2, а также квантильные оценки, предоставляют пользователям информацию о точности прогнозов и рисках. Графики временных рядов обеспечивают визуальное представление динамики цен, помогая инвесторам принимать обоснованные инвестиционные решения. Система регулярно обновляется с использованием новых данных, обеспечивая актуальность предсказаний и адаптацию к изменяющимся условиям рынка.


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
- [notebook](http://localhost/notebook) - пароль `N0t3b00l`

> После запуска проекта для интеграции *spark* в *airflow* не обходимо добавить Connection типа spark с параметрами: 
> - host: spark-master
> - name: spark_default
> - port: 7077

## Полезные материалы
- [Видео](https://disk.yandex.ru/d/61PQuQaTu8_HRw)
- [Дизайн](https://www.figma.com/file/0CaXixqbdbUVleztf2rwKY/Go-Algo?type=design&node-id=0%3A1&mode=design&t=we1CqdAZFJWcIc1f-1)
- [Презентация](https://docs.google.com/presentation/d/1h0BXlX0i7KvrXWzesCA-I6dnY6NxrIft/edit?usp=sharing&ouid=107107611917625953262&rtpof=true&sd=true)
- [UserFlow](https://miro.com/app/board/uXjVNEmEy7c=/)