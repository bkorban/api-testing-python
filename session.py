import json
import requests
from requests import RequestException
from logger import Logger


class HTTPSession:
    URL = 'https://jsonplaceholder.typicode.com/'

    # @staticmethod
    # def send_request(request_type, endpoint, data=None, params=None, headers=None):
    #     if data:
    #         response = request_type(endpoint, data=data, params=params)
    #     else:
    #         response = request_type(endpoint, params=params)

    #     do_logging = params.pop('do_logging', True)
    #     try:
    #         response = request_type(endpoint, params)
    #         if do_logging:
    #             Logger.log_request(request_type, endpoint,
    #                                params, response.status_code, data)
    #         return response.status_code, json.loads(response.text)
    #     except RequestException as e:
    #         Logger.log(
    #             'Could not send {} request due to exception: {}'.format(request_type, e))

    @staticmethod
    def send_request(request_type, endpoint, data=None, params=None, headers=None):
        do_logging = params.pop('do_logging', True) if params else True
        try:
            response = request_type(
                endpoint, data=data, params=params, headers=headers)
            if do_logging:
                Logger.log_request(request_type, endpoint,
                                    params, response.status_code, data, headers)
            return response.status_code, json.loads(response.text)
        except RequestException as e:
            Logger.log(
                'Could not send {} request due to exception: {}'.format(request_type, e))


class RequestTypes:
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    PATCH = requests.patch
    DELETE = requests.delete


class Endpoints:
    POSTS = HTTPSession.URL + 'posts'


class StatusCodes:
    STATUS_200 = '200'  # succeeded
    STATUS_201 = '201'  # created
