from airflow.plugins_manager import AirflowPlugin
from operators.reqres_operator import ReqResOperator


class ReqResAirflowPlugin(AirflowPlugin):
    name = "reqres"
    operators = [ReqResOperator]
