from flask import Response
from app.adapters.http.http_response_adapter import respond_api_error

def handle_exception(ex: Exception) -> Response:
    """
    Handle exceptions by generating an API error response.

    Args:
        ex (Exception): The exception to be handled.

    Returns:
        Response: The API error response generated from the exception.
    """
    return respond_api_error(
        ex.get_message(),
        ex.get_response_code()
    )
