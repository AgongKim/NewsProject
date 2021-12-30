import json
import random
import time

import requests
from bs4 import BeautifulSoup

from crawler.interactor import Interactor


class Crawler:
    def __init__(self):
        super().__init__()

    def notify_interactor(self, news_data, images):
        Interactor.notify_new_data(news_data, images)

    def get_response(self, url, params=None, check_keys=(), r_count=0):
        try:
            r_count += 1

            if r_count > 3:
                return []

            interval = random.uniform(0.2, 0.6)
            interval = round(interval, 1)
            time.sleep(interval)

            res = requests.get(url, params=params)
            res = json.loads(res.text)

            # check if response is valid
            for key in check_keys:
                if res == []:
                    continue
                if key in res:
                    continue
                else:
                    raise requests.exceptions.ConnectionError

        except requests.exceptions.ConnectionError:
            time.sleep(5)
            res = self.get_response(url, params=params, check_keys=check_keys, r_count=r_count)
        except ConnectionResetError:
            time.sleep(5)
            res = self.get_response(url, params=params, check_keys=check_keys, r_count=r_count)

        return res

    def get_response_bs4(self, url, params=None, check_keys=(), r_count=0):

        try:
            r_count += 1

            if r_count > 3:
                # if recursion is at 3, return empty list
                return []

            interval = random.uniform(0.2, 0.6)
            interval = round(interval, 1)
            time.sleep(interval)

            res = requests.get(url, params=params)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')

            for key in check_keys:
                if key in soup.text:
                    continue
                else:
                    raise requests.exceptions.ConnectionError

        except requests.exceptions.ConnectionError:
            time.sleep(5)
            soup = self.get_response_bs4(url, params=params, check_keys=check_keys, r_count=r_count)

        return soup
