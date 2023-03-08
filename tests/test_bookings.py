from asserter import assert_true, assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes, json
from test_utils import decorate_test, Constants, RequestParams, DataModel

ENDPOINT_BOOKING = Endpoints.BOOKING
ENDPOINT_HEALTHCHECK = Endpoints.PING

params = {RequestParams.booking_ID_key: RequestParams.booking_ID_value}
data = {}


class TestBookings:

    new_booking_id = None  # class attribute to store the new booking ID

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
        status_code, _ = HTTPSession.send_request(
            RequestTypes.GET, ENDPOINT_BOOKING)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT_BOOKING} enpoint')

    # acceptance testing
    # Feature: Create new booking
        # Scenario: User successfully creates new booking

    # Should create new booking, return code 200 and new booking details in json
    @staticmethod
    @decorate_test
    def test_booking_api_creates_new_booking():
        request_body = {
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
        headers = {'Content-Type': 'application/json'}
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

    @staticmethod
    @decorate_test
    def test_booking_api_gets_booking_by_id():
        # send GET request to retrieve the new booking
        headers = {'Content-Type': 'application/json'}

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
