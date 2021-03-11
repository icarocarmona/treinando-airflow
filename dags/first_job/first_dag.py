try:
    from first_job.engineering import get_data
    from first_job.task1 import first_function_execute
   
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd
    
    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))


# def first_function_execute(**context):
#     variable = context.get("name", "Didnt not get the key")
#     print("Hello {}".format(variable))
#     context['ti'].xcom_push(key='name_key', value='Push value Icaro Almeida') # ti = taskinstance


def second_function_execute(**context):
    value = context.get('ti').xcom_pull(key='name_key')
    print("XCom value : {}".format(value))
    get_data()
    
with DAG(
        dag_id="first_dag",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        }) as dag:

    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
        provide_context=True,
        op_kwargs={"name": "Icaro Carmona"}
    )

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
        provide_context=True,
    )

first_function_execute  >> second_function_execute

task1 >> [task2 , task3] >> task_join
