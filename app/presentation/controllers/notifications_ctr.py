from flask import Response, Blueprint, jsonify
from loguru import logger

from app.adapters.celery_broker_adapter import CeleryMessageBroker
from app.adapters.mongodb_adapter import MongoDBAdapter
from app.adapters.notification_processor_adapter import NotificationProcessor
from app.presentation.validation.notification_validator import validate_notifications_request
from app.domain.http.status_code import HttpStatusCode
from app.presentation.models.notifications_body import NotificationBody
from app.presentation.schemas.notifications import NotificationSchema
from app.presentation.validation.notification_validator import validate_notifications_request


mongodb = MongoDBAdapter()
celery = CeleryMessageBroker()
notification_processor = NotificationProcessor(mongodb, celery)
notifications_router = Blueprint("notifications_router", __name__)


@notifications_router.route("/notifications", methods=["POST"])
@validate_notifications_request(NotificationSchema)
def create_notification(body: NotificationBody) -> Response:
    """Creates a new customer notification"""
    logger.info(f"Received notification request: {body}")
    notification_processor.execute(body)
    return jsonify({"message": "Notification received successfully"}), HttpStatusCode.CREATED
