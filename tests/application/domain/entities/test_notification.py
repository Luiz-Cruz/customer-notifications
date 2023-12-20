from datetime import datetime, timedelta

from app.domain.entities.notification import Notification

class TestNotification:
    def test_init(self):
        """
        Test case to ensure correct initialization of a Notification object.
        Verifies that attributes are set correctly upon object creation.
        """
        user_id = "test_user"
        message = "Test message"
        notification_type = "TEST_TYPE"
        schedule_date = "2024-12-31 23:59:59"
        opt_out = True

        notification = Notification(user_id, message, notification_type, schedule_date, opt_out)

        assert notification.user_id == user_id
        assert notification.message == message
        assert notification.notification_type == notification_type
        assert notification.schedule_date == schedule_date
        assert notification.opt_out == opt_out

    def test_is_valid_schedule_date(self):
        """
        Test case to check the validity of the scheduled date for sending notifications.
        Covers scenarios where valid and invalid dates are provided.
        """
        notification = Notification("user_id", "Test message", "test_type")

        future_date = datetime.now() + timedelta(days=1)
        notification.schedule_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
        assert notification.is_valid_schedule_date

        past_date = datetime.now() - timedelta(days=1)
        notification.schedule_date = past_date.strftime("%Y-%m-%d %H:%M:%S")
        assert not notification.is_valid_schedule_date

        notification.schedule_date = "invalid_date_format"
        assert not notification.is_valid_schedule_date

    
    def test_to_dict(self):
        """
        Test case to validate the conversion of a Notification object to a dictionary.
        Checks if the dictionary representation is correct based on the presence of schedule_date.
        """
        
        notification = Notification("user_id", "Test message", "test_type")

        expected_dict = {
            "user_id": "user_id",
            "message": "Test message",
            "notification_type": "TEST_TYPE"
        }
        assert notification.to_dict == expected_dict

        notification.schedule_date = "2024-12-31 23:59:59"
        expected_dict_with_schedule = {
            "user_id": "user_id",
            "message": "Test message",
            "notification_type": "TEST_TYPE",
            "schedule_date": "2024-12-31 23:59:59"
        }
        assert notification.to_dict == expected_dict_with_schedule

    def test_notification_type_property(self):
        """
        Test case to validate the notification_type property's getter and setter.
        Checks if the getter returns the notification type in uppercase and the setter sets it correctly.
        """
        notification = Notification("user_id", "Test message", "test_type")
        assert notification.notification_type == "TEST_TYPE"
        notification.notification_type = "new_type"
        assert notification.notification_type == "NEW_TYPE"

    def test_repr(self):
        """
        Test case to ensure the __repr__ method of Notification works as expected.
        Verifies that the string representation contains key details of the Notification object.
        """
        user_id = "test_user"
        message = "Test message"
        notification_type = "TEST_TYPE"
        schedule_date = "2024-12-31 23:59:59"
        opt_out = True
        notification = Notification(user_id, message, notification_type, schedule_date, opt_out)
        expected_repr = f"Notification(user_id={user_id}, message={message}, notification_type={notification_type}, schedule_date={schedule_date}, opt_out={opt_out})"
        assert repr(notification) == expected_repr
