from dataclasses import dataclass


@dataclass
class NotificationsBody:
    """
    Represents the request body.

    :attr id: str
    :attr page: str
    """
    user_id: str
    message: str
    notification_type: str
    schedule_date: str = None
