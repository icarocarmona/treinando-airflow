from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from datetime import datetime


def second_function_execute(**context):
    nome = context.get("name", "Didnt not get the key")
    print("Hello {}".format(nome))
    # context['ti'].xcom_push(key='name_key', value='Push value Icaro Almeida') # ti = taskinstance

default_args = {
    "owner": "icaro",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2021, 1, 1),
}

with DAG(
        dag_id="second_dag",
        schedule_interval="@daily",
        default_args=default_args) as dag:

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
        provide_context=True,
        op_kwargs={"name": "Icaro Carmona"}
    )

second_function_execute
