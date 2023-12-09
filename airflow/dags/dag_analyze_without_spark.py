import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from algotrade.etl.analyze_without_spark import run as run_analyze


default_args = {
    "owner": "airflow",
    "retries": None,
}

dag_analyze_without_spark = DAG(
    dag_id="dag_analyze_without_spark",
    default_args=default_args,
    description="Analyze without spark",
    schedule=None,
    # schedule="*/5 * * * *",
    max_active_runs=1,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["algotrade"],
    catchup=False,
)


analyze_without_spark = PythonOperator(
    python_callable=run_analyze,
    task_id="analyze_without_spark",
    dag=dag_analyze_without_spark,
)

analyze_without_spark
