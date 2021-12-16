import json
import time
from threading import Thread

from loguru import logger
import requests
from requests.auth import HTTPBasicAuth

from main import Config


host = "127.0.0.1:8000"


def send_request(url, data):
    resp = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode("utf-8"), auth=HTTPBasicAuth(Config.user, Config.password))
    logger.info(f"{resp.status_code}, {resp.json()}")
    return resp


def redis_test():
    urls = [
        f"http://{host}/redis/lpush/",
        f"http://{host}/redis/rpop/",
    ]
    for i in range(3):
        for url in urls:
            print(url)
            value = {f"dslakjdlksa{i}": f"dsljakdjsal{i}"}
            value = {f"广州{i}": f"dsljakdjsal{i}"}
            data = {"db": 3, "key": "test", "value": value}
            t = Thread(target=send_request, args=(url, data,))
            t.start()
            time.sleep(0.1)


def mongo_test():
    url = f'http://{host}/mongo/insert/'
    for i in range(100):
        db = 'test'
        tablename = 'test'
        values = {'_id': i, 'values': f'value_{i}'}
        data = {'db': db, 'tablename': tablename, 'values': values}
        t = Thread(target=send_request, args=(url, data,))
        t.start()
        time.sleep(0.1)


if __name__ == "__main__":
    redis_test()
    mongo_test()
