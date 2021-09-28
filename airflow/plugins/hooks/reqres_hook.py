from airflow.hooks.http_hook import HttpHook
import requests
import json


class ReqResHook(HttpHook):

    def __init__(self, conn_id=None, page=None):
        self.page = page
        self.conn_id = conn_id or "reqres_default"
        super().__init__(http_conn_id=self.conn_id)

    def create_url(self):
        url = "https://reqres.in/api/users?page={}".format(
            self.page)
        return url

    def connect_to_endpoint(self, url, session):
        response = requests.Request("GET", url)
        prep = session.prepare_request(response)
        self.log.info(f"URL: {url}")
        return self.run_and_check(session, prep, {}).json()

    def run(self):
        session = self.get_conn()

        url = self.create_url()

        print(f"url:{url}")

        data = self.connect_to_endpoint(url, session)
        print(f"data:{data}")
        return data


if __name__ == "__main__":
    for pg in ReqResHook("ReqResHook").run():
        print(json.dumps(pg, indent=4, sort_keys=True))
