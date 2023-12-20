import os
from datetime import datetime

import pytz


NOTIFICATION_TYPES = ["EMAIL", "SMS", "WEB", "PUSH"]


class Notification:
    def __init__(self, user_id: str, message: str, notification_type: str, schedule_date: str = None):
        self.user_id = user_id
        self.message = message
        self.notification_type = notification_type
        self.schedule_date = schedule_date
    
    @property 
    def is_valid_schedule_date(self) -> bool:
        if self.schedule_date:
            try:
                timezone = pytz.timezone(os.getenv("TIMEZONE", "America/Sao_Paulo"))
                requested_schedule_date = datetime.strptime(self.schedule_date, "%Y-%m-%d %H:%M:%S")
                requested_schedule_date = timezone.localize(requested_schedule_date)
                current_datetime = datetime.now(timezone)
                if requested_schedule_date < current_datetime:
                    return False
            except ValueError:
                return False
        return True
    
    @property
    def to_dict(self) -> dict:
        return self.dict_to_schedule if self.schedule_date else self.dict_to_send
    
    @property
    def dict_to_schedule(self) -> dict:
        return {
            "user_id": self.user_id,
            "message": self.message,
            "notification_type": self.notification_type,
            "schedule_date": self.schedule_date
        }
    
    @property
    def dict_to_send(self) -> dict:
        return {
            "user_id": self.user_id,
            "message": self.message,
            "notification_type": self.notification_type
        }