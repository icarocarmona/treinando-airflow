from airflow.models.baseoperator import BaseOperator
from hooks.my_custom_hook import MyCustomHttpHook


class MyCustomOperator(BaseOperator):
    def __init__(self, conn_id=None, page=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.page = page
        self.ui_color = '#88FF00'
        self.ui_fgcolor = '#20322F'

    def execute(self, context):
        hook = MyCustomHttpHook(
            conn_id=self.conn_id,
            page=self.page
        )
        data = hook.run()
        print(data)

        return data
