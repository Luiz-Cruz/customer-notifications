from app.domain.entities.notification import Notification
from app.ports.notification_repository import NotificationRepository
from app.ports.notifications_strategy import NotificationStrategy

class WebNotificationStrategy(NotificationStrategy):
    """
    Strategy for handling web notifications.
    """

    def __init__(self, notification_repository: NotificationRepository):
        """
        Initialize the WebNotificationStrategy.

        Args:
            notification_repository (NotificationRepository): The repository for saving notifications.
        """
        self.notification_repository = notification_repository
        
    def execute(self, message: Notification) -> None:
        """
        Execute the strategy for web notifications.

        Args:
            message (Notification): The notification message to be handled.
        """
        self.notification_repository.save(message)
 
    def __repr__(self) -> str:
        """
            Returns a string representation of the WebNotificationStrategy object.

                This representation is used to display information about the instance
                of the WebNotificationStrategy class when used in the `repr()` function.
                
                Returns:
                    str: A string representation of the WebNotificationStrategy object.
        """
        return "WebNotificationStrategy"