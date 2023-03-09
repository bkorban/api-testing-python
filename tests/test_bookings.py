from asserter import assert_true, assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes, json
from test_utils import decorate_test, Constants, RequestParams, DataModel

ENDPOINT_BOOKING = Endpoints.BOOKING
ENDPOINT_HEALTHCHECK = Endpoints.PING
ENDPOINT_AUTH = Endpoints.AUTH

params = {RequestParams.booking_ID_key: RequestParams.booking_ID_value}
request_headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}

bookind_data = {
    "firstname": "James",
    "lastname": "Bond",
    "totalprice": 250,
    "depositpaid": True,
    "bookingdates": {
                "checkin": "2023-03-08",
                "checkout": "2023-03-30"
    },
    "additionalneeds": "Breakfast, Lunch and Dinner"
}

updated_booking_data = {
    "firstname": "James",
    "lastname": "Bond",
    "totalprice": 250,
    "depositpaid": True,
    "bookingdates": {
                "checkin": "2023-03-08",
                "checkout": "2023-03-30"
    },
    "additionalneeds": "No additional needs"
}

partial_updated_booking_data = {
    "firstname": "William"
}

booking_token_data = {
    "username": "admin",
    "password": "password123"
}


class TestBookings:

    new_booking_id = None  # class attribute to store the new booking ID
    token = None  # class attribute to store a token

    # health check endpoint to confirm whether API is up and running
    @staticmethod
    @decorate_test
    def test_booking_api_return_OK():
        status_code, _ = HTTPSession.send_request(
            RequestTypes.GET, ENDPOINT_HEALTHCHECK)
        assert_equal(status_code, StatusCodes.STATUS_201,
                     f'Status code of {ENDPOINT_HEALTHCHECK} enpoint')

    # validate response status code for get all bookings is 200
    @staticmethod
    @decorate_test
    def test_booking_api_status_code():
        headers = request_headers
        status_code, _ = HTTPSession.send_request(
            RequestTypes.GET, ENDPOINT_BOOKING, headers=headers)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT_BOOKING} enpoint')

    # Acceptance testing

    # Should create new booking, return code 200 and new booking details in json
    @staticmethod
    @decorate_test
    def test_booking_api_creates_new_booking():
        request_body = bookind_data
        headers = request_headers
        status_code, data = HTTPSession.send_request(
            RequestTypes.POST, ENDPOINT_BOOKING, data=json.dumps(request_body), headers=headers)
        responseBody_toJson = json.loads(data)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT_BOOKING} enpoint')
        assert_equal(responseBody_toJson['booking']
                     ['firstname'], 'James', 'firstname')
        assert_equal(responseBody_toJson['booking']
                     ['lastname'], 'Bond', 'lastname')
        assert_equal(responseBody_toJson['booking']
                     ['totalprice'], 250, 'totalprice')
        assert_equal(responseBody_toJson['booking']
                     ['depositpaid'], True, 'depositpaid')
        assert_equal(
            responseBody_toJson['booking']['bookingdates']['checkin'], '2023-03-08', 'checkin')
        assert_equal(
            responseBody_toJson['booking']['bookingdates']['checkout'], '2023-03-30', 'checkout')
        assert_equal(responseBody_toJson['booking']['additionalneeds'],
                     'Breakfast, Lunch and Dinner', 'additionalneeds')
        # store the booking id in the instance variable
        TestBookings.new_booking_id = responseBody_toJson['bookingid']
        if TestBookings.new_booking_id is not None:
            print("New booking ID:", TestBookings.new_booking_id)

    # send GET request to retrieve the new booking
    @staticmethod
    @decorate_test
    def test_booking_api_gets_booking_by_id():
        headers = request_headers

        status_code, data = HTTPSession.send_request(
            RequestTypes.GET, f"{ENDPOINT_BOOKING}/{TestBookings.new_booking_id}", headers=headers)
        responseBody_toJson = json.loads(data)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT_BOOKING}/{TestBookings.new_booking_id} endpoint')
        assert_equal(responseBody_toJson['firstname'], 'James', 'firstname')
        assert_equal(responseBody_toJson['lastname'], 'Bond', 'lastname')
        assert_equal(responseBody_toJson['totalprice'], 250, 'totalprice')
        assert_equal(responseBody_toJson['depositpaid'], True, 'depositpaid')
        assert_equal(responseBody_toJson['bookingdates']
                     ['checkin'], '2023-03-08', 'checkin')
        assert_equal(responseBody_toJson['bookingdates']
                     ['checkout'], '2023-03-30', 'checkout')
        assert_equal(responseBody_toJson['additionalneeds'],
                     'Breakfast, Lunch and Dinner', 'additionalneeds')

    # create a token for access to the PUT and DELETE booking
    @staticmethod
    @decorate_test
    def test_booking_api_creates_token():
        headers = request_headers
        request_body = booking_token_data
        status_code, data = HTTPSession.send_request(
            RequestTypes.POST, ENDPOINT_AUTH, data=json.dumps(request_body), headers=headers)
        responseBody_toJson = json.loads(data)

        assert_equal(status_code, StatusCodes.STATUS_200,
                     f"Status code of {ENDPOINT_AUTH} enpoint")
        # store the token in the instance variable
        TestBookings.token = responseBody_toJson['token']
        if TestBookings.token is not None:
            print("New token:", TestBookings.token)

    # send PUT request to update previously created booking
    @staticmethod
    @decorate_test
    def test_booking_api_update_current_booking():
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Cookie': f"token={TestBookings.token}"}
        request_body = updated_booking_data
        status_code, data = HTTPSession.send_request(
            RequestTypes.PUT, f"{ENDPOINT_BOOKING}/{TestBookings.new_booking_id}", data=json.dumps(request_body), headers=headers)
        responseBody_toJson = json.loads(data)

        assert_equal(status_code, StatusCodes.STATUS_200,
                     f"Status code of {ENDPOINT_BOOKING}/{TestBookings.new_booking_id} endpoint")
        assert_equal(responseBody_toJson['additionalneeds'],
                     'No additional needs', 'additionalneeds')

    # send PATCH request to update previously created booking with a partial payload
    @staticmethod
    @decorate_test
    def test_booking_api_partial_update_booking():
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Cookie': f"token={TestBookings.token}"}
        request_body = partial_updated_booking_data
        status_code, data = HTTPSession.send_request(
            RequestTypes.PATCH, f"{ENDPOINT_BOOKING}/{TestBookings.new_booking_id}", data=json.dumps(request_body), headers=headers)
        responseBody_toJson = json.loads(data)

        assert_equal(status_code, StatusCodes.STATUS_200,
                     f"Status code of {ENDPOINT_BOOKING}/{TestBookings.new_booking_id} endpoint")
        assert_equal(responseBody_toJson['firstname'], 'William', 'firstname')

    # send DELETE request to delete previously created booking
    @staticmethod
    @decorate_test
    def test_booking_api_delete_booking():
        headers = {'Content-Type': 'application/json',
                   'Cookie': f"token={TestBookings.token}"}
        status_code, _ = HTTPSession.send_request(
            RequestTypes.DELETE, f"{ENDPOINT_BOOKING}/{TestBookings.new_booking_id}", headers=headers)
        assert_equal(status_code, StatusCodes.STATUS_201,
                     f"Status code of {ENDPOINT_BOOKING}/{TestBookings.new_booking_id} endpoint")

    # send GET request to check if the recently deleted booking was successfully deleted

    @staticmethod
    @decorate_test
    def test_booking_api_gets_recenlty_deleted_booking_by_id():
        headers = request_headers
        status_code, _ = HTTPSession.send_request(
            RequestTypes.GET, f"{ENDPOINT_BOOKING}/{TestBookings.new_booking_id}", headers=headers)
        response_body = _
        assert_equal(status_code, StatusCodes.Status_404,
                     f"Status code of {ENDPOINT_BOOKING}/{TestBookings.new_booking_id} endpoint")
        assert_equal(response_body, 'Not Found', 'Response body')
