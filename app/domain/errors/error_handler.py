from flask import Response

from app.adapters.http_response_adapter import respond_api_error


def handle_exception(ex: Exception) -> Response:
    return respond_api_error(
        ex.get_message(),
        ex.get_response_code()
    )
    