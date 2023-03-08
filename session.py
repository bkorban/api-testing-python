import json
import requests
from requests import RequestException
from logger import Logger


class HTTPSession:
    URL = 'https://restful-booker.herokuapp.com/'

    # @staticmethod
    # def send_request(request_type, endpoint, data=None, params=None, headers=None):
    #     do_logging = params.pop('do_logging', True) if params else True
    #     try:
    #         response = request_type(endpoint, data=data,
    #                                 params=params, headers=headers)
    #         if do_logging:
    #             Logger.log_request(request_type, endpoint, params,
    #                             response.status_code, data, headers)
    #         if response.content:
    #             try:
    #                 return response.status_code, json.loads(response.text)
    #             except json.JSONDecodeError:
    #                 return response.status_code, None
    #         else:
    #             return response.status_code, None
    #     except RequestException as e:
    #         Logger.log(
    #             'Could not send {} request due to exception: {}'.format(request_type, e))

    @staticmethod
    def send_request(request_type, endpoint, data=None, params=None, headers=None):
        do_logging = params.pop('do_logging', True) if params else True
        try:
            response = request_type(endpoint, data=data, params=params, headers=headers)
            if do_logging:
                Logger.log_request(request_type, endpoint, params, response.status_code, data, headers)
            content_type = response.headers.get('Content-Type')
            if content_type == 'application/json':
                response_data = json.loads(response.text)
            else:
                response_data = response.text
            return response.status_code, response_data
        except RequestException as e:
            Logger.log('Could not send {} request due to exception: {}'.format(request_type, e))


class RequestTypes:
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    PATCH = requests.patch
    DELETE = requests.delete


class Endpoints:
    BOOKING = HTTPSession.URL + 'booking'
    PING = HTTPSession().URL + 'ping'


class StatusCodes:
    STATUS_200 = '200'  # succeeded
    STATUS_201 = '201'  # created
