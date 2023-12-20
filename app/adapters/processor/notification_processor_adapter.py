from dataclasses import asdict

from loguru import logger

from app.adapters.strategy.notification_strategies import NOTIFICATION_TYPES
from app.domain.entities.notification import Notification
from app.domain.errors.api_exception import ApiException
from app.domain.http.status_code import HttpStatusCode
from app.ports.message_broker import MessageBroker
from app.ports.user_repository import UserRepository
from app.presentation.models.notifications_body import NotificationBody

class NotificationProcessor:
    """Class responsible for processing notifications."""
    
    def __init__(self, user_repository: UserRepository, message_broker: MessageBroker):
        """
        Initialize the NotificationProcessor.

        Args:
            user_repository (UserRepository): An instance of the user repository.
            message_broker (MessageBroker): An instance of the message broker.
        """
        self.user_repository = user_repository
        self.message_broker = message_broker
    
    def execute(self, body: NotificationBody) -> None:
        """
        Execute the notification processing logic.

        Args:
            body (NotificationBody): The notification body data.

        Raises:
            ApiException: If there's an issue with the notification processing.
        """
        notification = Notification(**asdict(body))
        user_opt_out = self.user_is_opt_out(notification.user_id)
        
        if user_opt_out:
            logger.info("User opted out")
            raise ApiException("User has opted out of receiving notifications", HttpStatusCode.OK)
        
        if notification.notification_type not in NOTIFICATION_TYPES:
            logger.warning("Invalid notification type")
            raise ApiException("Invalid notification type", HttpStatusCode.BAD_REQUEST)
        
        if notification.schedule_date and not notification.is_valid_schedule_date:
            logger.warning("Invalid schedule date")
            raise ApiException("Invalid schedule date", HttpStatusCode.BAD_REQUEST)
        
        self.send_to_queue(notification.to_dict)
        
        
    def user_is_opt_out(self, user_id: str) -> bool:
        """
        Check if a user has opted out of notifications.

        Args:
            user_id (str): The ID of the user.

        Returns:
            bool: True if the user has opted out, False otherwise.

        Raises:
            ApiException: If the user is not found.
        """
        user = self.user_repository.find_by_id(user_id)
        if not user:
            logger.warning("User not found")
            raise ApiException("User not found", HttpStatusCode.BAD_REQUEST)

        return user.get("opt_out", False)
    
    def send_to_queue(self, notification: NotificationBody) -> None:
        """
        Send the notification to the message queue for processing.

        Args:
            notification (NotificationBody): The notification to be sent.

        Raises:
            ApiException: If there's an issue with sending the notification to the queue.
        """
        logger.info("Sending notification to the queue")
        self.message_broker.execute(notification)
