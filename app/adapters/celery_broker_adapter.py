import os

from celery import Celery

from app.ports.message_broker import MessageBroker

class CeleryMessageBroker(MessageBroker):
    def __init__(self):
        self.celery = Celery('customer-notifications', broker=os.getenv("CELERY_BROKER_URL"))
    
    def send_to_queue(self, message):
        self.celery.send_task(name="process-notifications", args=[message], queue="customer-notifications")
