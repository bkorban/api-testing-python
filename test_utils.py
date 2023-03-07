from datetime import timedelta
from time import time
from logger import Logger


def decorate_test(test_function):
    def wrapper():
        Logger.log_test_start(test_function)
        time_delta, _ = measure_time(test_function)
        Logger.log_test_finish(test_function, timedelta(seconds=time_delta))

    return wrapper


def measure_time(function):
    start = time()
    result = function()
    end = time()
    return end - start, result


class Constants:
    id = 'id'
    title = 'title'
    body = 'body'
    userId = 'userId'


class DataModel:
    posts_data_length = 100

class RequestParams:
    user_ID_key = 'userId',
    user_ID_value = 101



