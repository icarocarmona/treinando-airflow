from airflow import DAG
from airflow.contrib.operators import kubernetes_pod_operator
from airflow.models import Variable
from datetime import datetime, timedelta

import os

GCP_PROJECT = os.getenv('GCP_PROJECT')
NOME_DA_PESSOA = Variable.get("ENV")

default_args = {
    'owner': 'teste',
    'start_date': datetime(2021, 5, 31, 0, 0),
    'depends_on_past': False,   # run even if previous task failed
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

kube_resources = {
    'request_memory': '500Mi',
    'request_cpu': '500m',
    'limit_memory': '1Gi',
    'limit_cpu': 2
}

with DAG(
    'pod-testando-docker',
    default_args=default_args,
    schedule_interval='@daily',
    max_active_runs=1,
    catchup=False
) as dag:
    kubernetes_min_pod = kubernetes_pod_operator.KubernetesPodOperator(
        task_id='pod-testando-docker',
        name='pod-testando-docker',
        namespace='default',
        is_delete_operator_pod=True,
        resources=kube_resources,
        image=f'gcr.io/{GCP_PROJECT}/testando_docker:1',
        env_vars={
            "NOME_DA_PESSOA": NOME_DA_PESSOA
        },
    )
