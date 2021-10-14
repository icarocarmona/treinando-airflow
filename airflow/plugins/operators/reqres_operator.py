import json
from pathlib import Path

from airflow.models import BaseOperator, DAG, TaskInstance
from airflow.models.dag import DagTag
from airflow.utils.decorators import apply_defaults
from hooks.reqres_hook import ReqResHook
from datetime import datetime


class ReqResOperator(BaseOperator):
    template_fields = [
        "page"
    ]

    @apply_defaults
    def __init__(
        self,
        page,
        # file_path=,
        conn_id=None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        # self.file_path = file_path
        self.conn_id = conn_id

    # def create_parent_folder(self):
    #     Path(Path(self.file_path).parent).mkdir(parents=True, exist_ok=True)

    def execute(self, context):
        hook = ReqResHook(
            page=self.page,
            conn_id=self.conn_id
        )
        # self.create_parent_folder()
        data = hook.run()


if __name__ == "__main__":
    with DAG(dag_id="ReqResTeste",
             start_date=datetime.now()) as dag:
        to = ReqResOperator(
            page=1,
            task_id="teste_run")
        t1 = TaskInstance(to, datetime.now())
        to.execute(t1.get_template_context())
