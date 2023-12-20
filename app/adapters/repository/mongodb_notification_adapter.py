import os
from pymongo import MongoClient
from loguru import logger
from app.domain.entities.notification import Notification
from app.ports.notification_repository import NotificationRepository

class MongoDBNotificationAdapter(NotificationRepository):
    """
    Adapter for storing notifications in MongoDB.
    """

    def __init__(self):
        """
        Initialize the MongoDBNotificationAdapter.
        """
        self.client = MongoClient(os.environ.get('MONGO_URI'))
        self.db = self.client[os.environ.get('MONGO_DB', 'customer-notifications')] 

    def save(self, notification: Notification) -> dict:
        """
        Save a notification in the MongoDB.

        Args:
            notification (Notification): The notification object to be saved.

        Returns:
            dict: The saved notification data.
        """
        logger.info(f"Saving notification {notification}")
        try:
            self.db.notifications.insert_one({
                "user_id": notification.user_id,
                "message": notification.message,
            })
                 
            logger.info(f"Notification {notification} saved")
        except Exception as error:
            logger.error(f"Error saving notification {notification}: {error}")
            return False

            
   
