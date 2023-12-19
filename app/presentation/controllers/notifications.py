import os

from flask import Response, Blueprint, jsonify

from app.adapters.celery_queue_adapter import CeleryAdapter
from app.adapters.notifications_service_adapter import QueueProcessor
from app.domain.http.status_code import HttpStatusCode
from app.presentation.models.notifications_body import NotificationBody
from app.presentation.schemas.notifications import NotificationSchema
from app.presentation.validation.notification_validator import validate_notifications_request

broker_url = os.getenv("CELERY_BROKER_URL")
notifications_router = Blueprint("notifications_router", __name__)


@notifications_router.route("/notifications", methods=["POST"])
@validate_notifications_request(NotificationSchema)
def create_notification(notification: NotificationBody) -> Response:
    """Creates a new customer notification"""
    message_broker = CeleryAdapter(broker_url, "customer_notifications")
    queue_processor = QueueProcessor(message_broker)
    queue_processor.execute(notification)
    return jsonify({"message": "Notification received successfully"}), HttpStatusCode.CREATED
