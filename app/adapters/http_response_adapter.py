import json

from flask import Response

from app.domain.http.status_code import HttpStatusCode


def respond_created_successfully() -> Response:
    """
    Respond with created successfully

    Returns:
        Response: Flask response
    """
    return Response(
        json.dumps({
            "status": HttpStatusCode.CREATED,
            "message": "Notifications received successfully.",
        }),
        mimetype='application/json',
        status=HttpStatusCode.CREATED
    )
