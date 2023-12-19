from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError
from loguru import logger
from app.domain.errors.bad_request import BadRequest

from app.presentation.models.notifications_body import NotificationBody

def validate_notifications_request(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_data = request.get_json()
            try:
                data = schema().load(json_data)
                validated_data = NotificationBody(**data)
                return func(validated_data, *args, **kwargs)
            except ValidationError as err:
                raise BadRequest(f"Invalid request body, missing: {err.messages}")            
        return wrapper
    return decorator
