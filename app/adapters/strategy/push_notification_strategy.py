
from app.domain.entities.notification import Notification
from app.ports.notifications_strategy import NotificationStrategy


class PushNotificationStrategy(NotificationStrategy):
    def __init__(self):
        ... # TODO
        
    def execute(self, message: Notification) -> None:
        ... # TODO
