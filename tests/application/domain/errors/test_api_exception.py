from app.domain.errors.api_exception import ApiException


class TestApiException:
    def test_init(self):
        """
        Test case to validate the initialization of ApiException.
        Verifies that attributes message and response_code are set correctly.
        """
        message = "Test message"
        response_code = 404

        exception = ApiException(message, response_code)

        assert exception.message == message
        assert exception.response_code == response_code

    def test_get_response_code(self):
        """
        Test case to check the get_response_code method of ApiException.
        Verifies that the method returns the correct response code.
        """
        message = "Test message"
        response_code = 404

        exception = ApiException(message, response_code)

        assert exception.get_response_code() == response_code

    def test_get_message(self):
        """
        Test case to validate the get_message method of ApiException.
        Verifies that the method returns the correct message.
        """
        message = "Test message"
        response_code = 404

        exception = ApiException(message, response_code)

        assert exception.get_message() == message
