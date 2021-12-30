from datetime import datetime, timedelta
from threading import Thread

from crawler.crawler import Crawler


class DaumCrawler(Crawler):
    _rank_news_url = 'https://news.daum.net/ranking/popular'

    def __init__(self):
        super.__init__()
        self._is_running = False

    def crawl(self):
        if not self._is_running:
            self._is_running = True
            thread = Thread(target=self._run)
            thread.daemon = True
            thread.start()
        else:
            error_text = 'ERROR : 다음 크롤러 동작중'
            # error alert here

    def run(self):
        speed = 4

        thread_list = list()
        thread_count = speed

    def _pass_data_to_interactor(self):
        date_list = self._get_date_list()
        try:
            for date in date_list:
                news_generator = self._get_news_generator(date)


    def _get_date_list(self):
        #date format = YYYYmmdd
        date_list = []
        end = datetime.now()
        start = end - timedelta(days=30)
        dates = [(start + timedelta(days=i)) for i in range((end - start).days + 1)]
        for date in dates:
            date_list.append(f'{date:%Y%m%d}')
        return date_list

    def _get_news_generator(self, date):
        url = self._rank_news_url+f'?regDate={date}'
        check_keys = ['뉴스']
