import requests
import json
from loguru import logger


def create_url():
    page = 2
    url = "https://reqres.in/api/users?page={}".format(
        page
    )
    return url


def get_data(url, headers=None):
    response = requests.request("GET", url, headers=headers)
    logger.info(f"Status code:{response.status_code}")
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    url = create_url()
    json_response = get_data(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
