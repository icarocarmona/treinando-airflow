from datetime import datetime, timedelta
from pprint import pprint

from airflow.utils.dates import days_ago

from airflow.models import DAG, TaskInstance
from operators.reqres_operator import ReqResOperator
from os.path import join

args = {
    'owner': 'Airflow',
    'start_date': days_ago(2),
}


with DAG(dag_id="ReqResTest", start_date=datetime.now()) as dag:
    to = ReqResOperator(
        page=2,
        file_path=join(
            "/home/icaro/Projects/treinando-airflow/datalake",
            "data_reqres",
            "extract_date={{ ds }}",
            "ReqRes_{{ ds_nodash }}.json"
        ),
        task_id="test_run"
    )
    ti = TaskInstance(
        task=to, execution_date=datetime.now() - timedelta(days=1))
    ti.run()
