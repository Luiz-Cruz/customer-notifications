
from app.adapters.repository.mongodb_notification_adapter import MongoDBNotificationAdapter
from app.adapters.strategy.email_notification_adapter import EmailNotificationStrategy
from app.adapters.strategy.push_notification_strategy import PushNotificationStrategy
from app.adapters.strategy.sms_notification_adapter import SmsNotificationStrategy
from app.adapters.strategy.web_notification_strategy import WebNotificationStrategy

web_notification_repository = MongoDBNotificationAdapter()

NOTIFICATION_STRATEGIES = {
    "EMAIL": EmailNotificationStrategy(),
    "SMS": SmsNotificationStrategy(),
    "WEB": WebNotificationStrategy(web_notification_repository),
    "PUSH": PushNotificationStrategy()
}

NOTIFICATION_TYPES = ["EMAIL", "SMS", "WEB", "PUSH"]
