import pytest
from unittest.mock import MagicMock
from app.domain.entities.notification import Notification
from app.ports.notification_repository import NotificationRepository
from app.ports.notifications_strategy import NotificationStrategy
from app.adapters.strategy.web_notification_strategy import WebNotificationStrategy

class TestWebNotificationStrategy:
    def test_init(self):
        """
        Test case to verify the initialization of WebNotificationStrategy.
        Ensures that the notification repository is properly set during initialization.
        """
        notification_repo = MagicMock(NotificationRepository)
        web_strategy = WebNotificationStrategy(notification_repo)
        assert web_strategy.notification_repository == notification_repo

    def test_execute(self):
        """
        Test case to validate the execution of the WebNotificationStrategy.
        Verifies that the strategy correctly saves the notification using the repository.
        """
        notification_repo = MagicMock(NotificationRepository)
        web_strategy = WebNotificationStrategy(notification_repo)
        notification = Notification(user_id="user_id", message="Test message", notification_type="WEB")
        web_strategy.execute(notification)
        notification_repo.save.assert_called_once_with(notification)

    def test_repr(self):
        """
        Test case to ensure the __repr__ method of WebNotificationStrategy works as expected.
        Verifies that the method returns a string representation of the object.
        """
        notification_repo = MagicMock(NotificationRepository)
        web_strategy = WebNotificationStrategy(notification_repo)
        expected_repr = "WebNotificationStrategy"
        assert repr(web_strategy) == expected_repr
