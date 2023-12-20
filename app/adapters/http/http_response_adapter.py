import json

from flask import Response


def respond_api_error(error_details: str, status_code: int) -> Response:
    """
    Respond with api error

    Args:
        error_details (str): Error details
        status_code (int): Status code

    Returns:
        Response: Flask response
    """
    return Response(
        json.dumps(
            {
                "message": error_details,
                "status": status_code,
            }
        ),
        mimetype='application/json',
        status=status_code
    )