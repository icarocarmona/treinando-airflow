from configparser import NoOptionError
from operators.my_custom_operator import MyCustomOperator
from airflow.models.dag import DAG
from datetime import datetime

with DAG(
    dag_id='custom_operator',
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
) as dag:
    hello_task = MyCustomOperator(
        task_id="sample-custom-operator", page=1)


hello_task
