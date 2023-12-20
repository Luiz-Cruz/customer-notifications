from dataclasses import dataclass


@dataclass
class NotificationBody:
    """
    Represents the request body.

    :attr user_id: str
    :attr message: str
    :attr notification_type: str
    :attr schedule_date: str
    """
    user_id: str
    message: str
    notification_type: str
    schedule_date: str = None
    