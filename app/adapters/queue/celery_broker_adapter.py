import os
from celery import Celery
from app.ports.message_broker import MessageBroker

class CeleryMessageBroker(MessageBroker):
    """
    A message broker utilizing Celery for sending messages/tasks.
    """

    def __init__(self):
        """
        Initialize the CeleryMessageBroker.
        """
        self.celery = Celery('customer-notifications', broker=os.environ.get("CELERY_BROKER_URL"))
    
    def execute(self, message):
        """
        Execute the sending of a message/task via Celery.

        Args:
            message: The message/task to be sent.
        """
        self.celery.send_task(name="customer-notifications", args=[message], queue="customer-notifications")
