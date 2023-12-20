import os

import pytz


from datetime import datetime


class Notification:
    """A class representing a notification to be sent."""

    def __init__(self, user_id: str, message: str, notification_type: str, schedule_date: str = None, opt_out: bool = None):
        """
        Initialize a Notification object.

        Args:
            user_id (str): The ID of the user receiving the notification.
            message (str): The message content of the notification.
            notification_type (str): The type of notification.
            schedule_date (str, optional): The date and time to schedule the notification. Defaults to None.
            opt_out (bool, optional): A flag indicating if the user has opted out of notifications. Defaults to None.
        """
        self.user_id = user_id
        self.message = message
        self.notification_type = notification_type
        self.schedule_date = schedule_date
        self.opt_out = opt_out
    
    @property
    def is_valid_schedule_date(self) -> bool:
        """
        Check if the scheduled date is valid for sending the notification.

        Returns:
            bool: True if the scheduled date is in the future, False otherwise.
        """
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
        """
        Convert the Notification object to a dictionary based on the presence of schedule_date.

        Returns:
            dict: Dictionary representation of the notification data.
        """
        return self.dict_to_schedule if self.schedule_date else self.dict_to_send
    
    @property
    def dict_to_schedule(self) -> dict:
        """
        Create a dictionary representation of the notification data with schedule_date.

        Returns:
            dict: Dictionary representation of the notification data with schedule_date.
        """
        return {
            "user_id": self.user_id,
            "message": self.message,
            "notification_type": self.notification_type,
            "schedule_date": self.schedule_date
        }
    
    @property
    def dict_to_send(self) -> dict:
        """
        Create a dictionary representation of the notification data without schedule_date.

        Returns:
            dict: Dictionary representation of the notification data without schedule_date.
        """
        return {
            "user_id": self.user_id,
            "message": self.message,
            "notification_type": self.notification_type
        }
        
    @property
    def notification_type(self) -> str:
        """
        Get the notification type.

        Returns:
            str: The notification type in uppercase.
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str) -> None:
        """
        Set the notification type in uppercase.

        Args:
            notification_type (str): The notification type.
        """
        self._notification_type = notification_type.upper()

    def __repr__(self):
        """
        Returns a string representation of the Notification object.

        This representation includes information about the Notification instance,
        such as user_id, message, notification_type, schedule_date, and opt_out.
        
        Returns:
            str: A string representation containing key details of the Notification object.
        """
        return f"Notification(user_id={self.user_id}, message={self.message}, notification_type={self.notification_type}, schedule_date={self.schedule_date}, opt_out={self.opt_out})"
