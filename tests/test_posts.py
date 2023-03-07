from asserter import assert_true, assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes, json
from test_utils import decorate_test, Constants, RequestParams, DataModel

ENDPOINT = Endpoints.POSTS

params = {RequestParams.user_ID_key: RequestParams.user_ID_value}
data = {}


class TestPosts:

    # validate response status code for get all posts is 200
    @staticmethod
    @decorate_test
    def test_posts_api_status_code():
        status_code, _ = HTTPSession.send_request(
            RequestTypes.GET, ENDPOINT, params)
        assert_equal(status_code, StatusCodes.STATUS_200,
                     f'Status code of {ENDPOINT} enpoint')

    # validate posts data length is 100
    @staticmethod
    @decorate_test
    def test_posts_api_returned_list_length():
        _, posts_data = HTTPSession.send_request(
            RequestTypes.GET, ENDPOINT, params)
        assert_equal(len(posts_data), DataModel().posts_data_length,
                     'Number of posts returned by data response:')

    # acceptance testing
    # Feature: Retrieve post data
        # Scenario: User request particular post data

    # Should return post by id when post id exists
    # @staticmethod
    # @decorate_test
    # def test_posts_api_returned_specified_post_by_postId():
    #     _, posts_data = HTTPSession.send_request(
    #         RequestTypes.GET, ENDPOINT, params.pop(RequestParams.user_ID_key))
    #     assert_true(value, message)

    # Should create new post and returned status code 201 with the response body matching the request body
    @staticmethod
    @decorate_test
    def test_posts_api_creates_new_post():
        request_body = {
            'title': 'New Post Title',
            'body': 'New Post Body',
            'userId': 1
        }
        headers = {'Content-Type': 'application/json'}
        status_code, posts_data = HTTPSession.send_request(
            RequestTypes.POST, ENDPOINT, data=json.dumps(request_body), headers=headers)
        assert_equal(status_code, StatusCodes.STATUS_201,
                     f'Status code of {ENDPOINT} enpoint')
        assert_equal(posts_data['title'], 'New Post Title', 'New post title')
        assert_equal(posts_data['body'], 'New Post Body', 'New post body')
        assert_true('id' in posts_data, 'New post ID was returned')
