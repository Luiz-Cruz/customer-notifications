from datetime import datetime

from marshmallow import Schema, fields

from app.domain.errors.bad_request import BadRequest


def validate_notification_type(notification_type):
    if notification_type not in ['email', 'sms', 'push']:
        raise BadRequest(f"Invalid notification type: {notification_type}")
    return notification_type


def validate_schedule_date(schedule_date):
    if schedule_date:
        try:
            datetime.strptime(schedule_date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise BadRequest(f"Invalid schedule date: {schedule_date}, expected format: YYYY-MM-DD HH:MM:SS")
    return schedule_date


class NotificationSchema(Schema):
    """
    Represents the request schema for the sitelink automation.

    :attr user_id: str
    :attr message: str
    :attr notification_type: str
    :attr schedule_date: str (optional)
    """
    user_id = fields.Str(required=True)
    message = fields.Str(required=True)
    notification_type = fields.Str(required=True, validate=validate_notification_type)
    schedule_date = fields.Str(required=False, validate=validate_schedule_date)
