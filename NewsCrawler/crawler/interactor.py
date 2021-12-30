from collections import deque
from threading import Lock, Thread
from django.db.utils import OperationalError

class Interactor:
    _news_data = deque()
    _update_data = dict()
    _lock = Lock()
    _is_working = False

    @staticmethod
    def notify_new_data(news_data, images):
        Interactor._news_data.append((news_data, images))
        Interactor._lock.acquire()
        Interactor._interact()
        Interactor._lock.release()

    @staticmethod
    def _interact():
        if not Interactor._is_working:
            Interactor._is_working = True
            thread = Thread(target=Interactor._run)
            thread.daemon = True
            thread.start()

    @staticmethod
    def _run():
        pass
        # while True:
        #     current_tuple = ()
        #     try:
        #         if len(Interactor._news_data) > 0:
        #             data_tuple = Interactor._news_data.popleft()
        #             current_tuple = data_tuple
        #     except IndexError as e:
        #         is_exist = Interactor._news_data_empty()
        #         if is_exist:
        #             continue
        #         else:
        #             break
        #     except OperationalError:
        #         Interactor._

    # @staticmethod
    # def _news_data_empty():
    #     if Interactor._update_data.__len__() > 0:
