from airflow.plugins_manager import AirflowPlugin
from operators.my_custom_operator import MyCustomOperator


class ReqResAirflowPlugin(AirflowPlugin):
    name = "mycustomoperator"
    operators = [MyCustomOperator]
