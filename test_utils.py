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
    bookingid: 'bookingid'
    booking: 'booking'
    firstname: 'firstname'
    lastname: 'lastname'
    totalprice: 'totalprice'
    depositpaid: 'depositpaid'
    bookingdates: 'bookingdates'
    checkin: 'checkin'
    checkout: 'checkout'
    additionalneeds: 'additionalneeds'
    


class DataModel:
    bookings_data_length = None

class RequestParams:
    booking_ID_key = 'bookingid',
    booking_ID_value = 1



