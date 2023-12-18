from marshmallow import Schema, fields


class NotificationsSchema(Schema):
    """
    Represents the request schema for the sitelink automation.

    :attr user_id: str
    :attr message: str
    :attr notification_type: str
    :attr schedule_date: str
    """
    user_id = fields.Str(required=True)
    message = fields.Str(required=True)
    notification_type = fields.Str(required=True)
    schedule_date = fields.Str(required=False)
