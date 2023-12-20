import pytest

from unittest.mock import MagicMock, patch

from app.adapters.processor.notification_processor_adapter import NotificationProcessor
from app.domain.errors.api_exception import ApiException
from app.domain.http.status_code import HttpStatusCode
from app.presentation.models.notifications_body import NotificationBody



def test_user_opt_out():
    """
    Test case to check behavior when a user has opted out of notifications.
    Verifies that an ApiException is raised and the proper response code is set.
    """
    mock_user_repository = MagicMock()
    mock_message_broker = MagicMock()
    
    mock_user_repository.find_by_id.return_value = {
        "user_id": "some_user_id",
        "opt_out": True,
        "email": "email@email",
    }
    
    notification_body = NotificationBody(
        user_id="some_user_id",
        message="some_message",
        notification_type="WEB",
    )
     
    notification_processor = NotificationProcessor(mock_user_repository, mock_message_broker)
    
    with pytest.raises(ApiException) as exception:
        notification_processor.execute(notification_body)
    
    mock_user_repository.find_by_id.assert_called_once_with("some_user_id")
    mock_message_broker.send_to_queue.assert_not_called()
    assert "User has opted out of receiving notifications" in str(exception)
    assert exception.value.response_code == HttpStatusCode.OK


def test_invalid_notification_type():
    """
    Test case to validate behavior when an invalid notification type is provided.
    Verifies that an ApiException is raised with the appropriate response code.
    """
    mock_user_repository = MagicMock()
    mock_message_broker = MagicMock()
    
    mock_user_repository.find_by_id.return_value = {
        "user_id": "some_user_id",
        "opt_out": False,
        "notification_type": "OTHER",
    }
    
    notification_body = NotificationBody(
        user_id="some_user_id",
        message="some_message",
        notification_type="OTHER",
    )
    
    notification_processor = NotificationProcessor(mock_user_repository, mock_message_broker)
    
    with pytest.raises(ApiException) as exception:
        notification_processor.execute(notification_body)
        assert "Invalid notification type" in str(e)
        
    mock_user_repository.find_by_id.assert_called_once_with("some_user_id")
    mock_message_broker.send_to_queue.assert_not_called()
    assert "Invalid notification type" in str(exception)
    assert exception.value.response_code == HttpStatusCode.BAD_REQUEST
    
    
def test_invalid_schedule_date():
    """
    Test case to verify behavior when an invalid schedule date is provided.
    Checks that an ApiException is raised and the response code is set accordingly.
    """
    mock_user_repository = MagicMock()
    mock_message_broker = MagicMock()
    
    mock_user_repository.find_by_id.return_value = {
        "user_id": "some_user_id",
        "opt_out": False,
        "notification_type": "WEB",
    }
    
    notification_body = NotificationBody(
        user_id="some_user_id",
        message="some_message",
        notification_type="WEB",
        schedule_date="2021-01-01",
    )
    
    notification_processor = NotificationProcessor(mock_user_repository, mock_message_broker)
    
    with pytest.raises(ApiException) as exception:
        notification_processor.execute(notification_body)
    
    mock_user_repository.find_by_id.assert_called_once_with("some_user_id")
    mock_message_broker.send_to_queue.assert_not_called()
    assert "Invalid schedule date" in str(exception)
    assert exception.value.response_code == HttpStatusCode.BAD_REQUEST
    
    
def test_notification_processor():
    """
    Test case to ensure the NotificationProcessor behaves correctly.
    Validates that the processor handles the notification properly.
    """
    with patch('app.domain.entities.notification.Notification') as mock_notification:
        mock_notification_instance = mock_notification.return_value
        mock_notification_instance.user_id = 'some_user_id'
        mock_notification_instance.notification_type = 'WEB'
       
        mock_user_repository = MagicMock()
        mock_message_broker = MagicMock()
        mock_user_repository.find_by_id.return_value = {
            "user_id": "some_user_id",
            "opt_out": False,
            "notification_type": "WEB",
        }

        notification_body = NotificationBody(
            user_id="some_user_id",
            message="some_message",
            notification_type="WEB",
            schedule_date="2024-01-01 12:00:00", 
        )
        

        notification_processor = NotificationProcessor(mock_user_repository, mock_message_broker)
        notification_processor.execute(notification_body)

        mock_user_repository.find_by_id.assert_called_once_with("some_user_id")
        mock_message_broker.execute.assert_called is True 
        