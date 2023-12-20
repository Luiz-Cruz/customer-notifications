from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError
from loguru import logger
from app.domain.errors.bad_request import BadRequest
from app.presentation.models.notifications_body import NotificationBody

def validate_notifications_request(schema):
    """
    Validate notifications request decorator.

    Args:
        schema: The schema used for validation.

    Returns:
        function: Decorator function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function to validate notifications request.

            Args:
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.

            Raises:
                BadRequest: If the request body is invalid.

            Returns:
                Response: Response from the decorated function.
            """
            json_data = request.get_json()
            try:
                data = schema().load(json_data)
                validated_data = NotificationBody(**data)
                return func(validated_data, *args, **kwargs)
            except ValidationError as err:
                raise BadRequest(f"Invalid request body: {err.messages}")            
        return wrapper
    return decorator
