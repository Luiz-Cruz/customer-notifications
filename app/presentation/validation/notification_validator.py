from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError

from app.presentation.models.notifications_body import NotificationBody


def validate_notifications_request(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                json_data = request.get_json()
                data = schema.load(json_data)
                validated_data = NotificationBody(**data)
                return func(validated_data, *args, **kwargs)
            except ValidationError as err:
                return jsonify({'error': err.messages}), 400
        return wrapper
    return decorator
