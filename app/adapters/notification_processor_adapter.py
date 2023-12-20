from dataclasses import asdict

from loguru import logger

from app.domain.entities.notification import NOTIFICATION_TYPES, Notification
from app.domain.errors.api_exception import ApiException
from app.domain.http.status_code import HttpStatusCode
from app.ports.message_broker import MessageBroker
from app.ports.user_repository import UserRepository
from app.presentation.models.notifications_body import NotificationBody


class NotificationProcessor:
    def __init__(self, user_repository: UserRepository, message_broker: MessageBroker):
        self.user_repository = user_repository
        self.message_broker = message_broker
    
    def execute(self, body: NotificationBody) -> None:
        notification = Notification(**asdict(body))
        user_opt_out = self.user_is_opt_out(notification.user_id)
        
        if user_opt_out:
            logger.info("User opted out")
            raise ApiException("User has opted out of receiving notifications", HttpStatusCode.OK)
        
        if notification.notification_type.upper() not in NOTIFICATION_TYPES:
            logger.warning("Invalid notification type")
            raise ApiException("Invalid notification type", HttpStatusCode.BAD_REQUEST)
        
        if notification.schedule_date and notification.is_valid_schedule_date:
            logger.info(f"Scheduling notification for {notification.schedule_date}")
            self.send_to_queue(notification.to_dict)
        
        if notification.schedule_date and not notification.is_valid_schedule_date:
            logger.warning("Invalid schedule date")
            raise ApiException("Invalid schedule date", HttpStatusCode.BAD_REQUEST)
        
        
    def user_is_opt_out(self, user_id: str) -> bool:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            logger.warning("User not found")
            raise ApiException("User not found", HttpStatusCode.BAD_REQUEST)

        return user.get("opt_out", False)
    
    def send_to_queue(self, notification: NotificationBody) -> None:
        logger.info("Sending notification to the queue")
        self.message_broker.send_to_queue(notification)
