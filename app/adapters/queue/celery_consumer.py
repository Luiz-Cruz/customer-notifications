import os
from typing import List
from celery import Celery
from celery import bootsteps
from flask import jsonify
from kombu import Consumer, Queue, Message
from loguru import logger
from app.adapters.strategy.notification_strategies import NOTIFICATION_STRATEGIES
from app.domain.entities.notification import Notification

customer_queue = Queue('customer-notifications')
app = Celery(broker=os.environ['CELERY_BROKER_URL'])

class NotificationService(bootsteps.ConsumerStep):
    """
    Service responsible for consuming and processing notification messages.
    """

    def get_consumers(self, channel: object):
        """
        Get the consumers for processing messages from the customer notifications queue.

        Args:
            channel: The channel for message consumption.

        Returns:
            list: List of consumers for the specified queue.
        """
        return [Consumer(channel, queues=[customer_queue], callbacks=[self.handle_message], accept=['json'])]

    def handle_message(self, body: List, queued_message: Message) -> None:
        """
        Handle the incoming notification message.

        Args:
            body (List): The body of the incoming message.
            queued_message (Message): The queued message object.
        """
        logger.info(f"Received message: {body}")
        notification = self.format_message(body)
        notification_strategy = NOTIFICATION_STRATEGIES[notification.notification_type]
        logger.info(f"Using strategy: {notification_strategy}")
        
        if not notification.schedule_date:
            logger.info(f"Sending notification immediately")
            notification_strategy.execute(notification)
        
        if notification.schedule_date:
            logger.info(f"Scheduling notification for {notification.schedule_date}")
            notification_strategy.execute.apply_async(args=[notification], eta=notification.schedule_date)        
        
        logger.info(f"Acknowledging message {queued_message}")
        queued_message.ack()
        return jsonify({"message": "Notification processed successfully"}), 200
    
    @staticmethod
    def format_message(body: List):
        """
        Format the incoming message body into a Notification object.

        Args:
            body (List): The body of the incoming message.

        Returns:
            Notification: A Notification object created from the body.
        """
        notification = body[0][0]
        user_id = notification.get('user_id')
        message = notification.get('message')
        notification_type = notification.get('notification_type')
        opt_out = notification.get('opt_out')
        return Notification(user_id, message, notification_type, opt_out)

    def schedule_message(self, notification: Notification):
        """
        Schedule a notification message.

        Args:
            notification (Notification): The notification to be scheduled.
        """
        logger.info(f"Scheduling notification for {notification.schedule_date}")

app.steps['consumer'].add(NotificationService)
