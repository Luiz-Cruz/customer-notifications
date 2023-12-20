from app.domain.http.status_code import HttpStatusCode
from app.domain.errors.bad_request import BadRequest

class TestBadRequest:
    def test_init(self):
        """
        Test case to validate the initialization of BadRequest.
        Verifies that the error message and response code are set correctly.
        """
        error_msg = "Bad request error"
        bad_request = BadRequest(error_msg)
        assert bad_request.message == error_msg
        assert bad_request.response_code == HttpStatusCode.BAD_REQUEST

    def test_get_response_code(self):
        """
        Test case to check the inheritance of get_response_code method in BadRequest.
        Verifies that the method returns the correct response code from ApiException.
        """
        error_msg = "Bad request error"
        bad_request = BadRequest(error_msg)
        assert bad_request.get_response_code() == HttpStatusCode.BAD_REQUEST

    def test_get_message(self):
        """
        Test case to validate the inheritance of get_message method in BadRequest.
        Verifies that the method returns the correct message from ApiException.
        """
        error_msg = "Bad request error"
        bad_request = BadRequest(error_msg)
        assert bad_request.response_code == HttpStatusCode.BAD_REQUEST
        assert bad_request.message == error_msg
