import pendulum
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 


default_args = {
    "owner": "airflow",
    "retries": None,
}

dag_analyze = DAG(
    dag_id="dag_analyze",
    default_args=default_args,
    description="Analyze",
    schedule=None,
    # schedule="0 0 * * 3",
    max_active_runs=1,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["algotrade"],
    catchup=False,
)


clickhouse_to_parquet = SparkSubmitOperator(
    application='/opt/airflow/dags/algotrade/etl/clickhouse_to_parquet.py',
    conn_id='spark_default',
    verbose=1,
    task_id='clickhouse_to_parquet', 
    dag=dag_analyze
)

parquet_to_clickhouse = SparkSubmitOperator(
    application='/opt/airflow/dags/algotrade/etl/parquet_to_clickhouse.py',
    conn_id='spark_default',
    verbose=1,
    task_id='parquet_to_clickhouse', 
    dag=dag_analyze
)

analyze = SparkSubmitOperator(
    application='/opt/airflow/dags/algotrade/etl/analyze.py',
    conn_id='spark_default',
    verbose=1,
    task_id='analyze', 
    dag=dag_analyze
)

clickhouse_to_parquet >> [analyze] >> parquet_to_clickhouse
