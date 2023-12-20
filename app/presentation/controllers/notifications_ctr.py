from flask import Response, Blueprint, jsonify
from loguru import logger

from app.adapters.queue.celery_broker_adapter import CeleryMessageBroker
from app.adapters.repository.mongodb_notification_adapter import MongoDBNotificationAdapter
from app.adapters.repository.user_mongodb_adapter import UserRepositoryMongoDBAdapter
from app.adapters.processor.notification_processor_adapter import NotificationProcessor
from app.domain.entities.notification import Notification
from app.presentation.validation.notification_validator import validate_notifications_request
from app.domain.http.status_code import HttpStatusCode
from app.presentation.models.notifications_body import NotificationBody
from app.presentation.schemas.notifications import NotificationSchema
from app.presentation.validation.notification_validator import validate_notifications_request


mongodb = UserRepositoryMongoDBAdapter()
celery = CeleryMessageBroker()
notification_processor = NotificationProcessor(mongodb, celery)
notifications_router = Blueprint("notifications_router", __name__)


@notifications_router.route("/notifications", methods=["POST"])
@validate_notifications_request(NotificationSchema)
def create_notification(body: NotificationBody) -> Response:
    """Creates a new customer notification"""
    logger.info(f"Received notification request: {body}")
    notification_processor.execute(body)
    return jsonify({
        "message": "Notification received successfully", 
        "status": HttpStatusCode.CREATED
    }), HttpStatusCode.CREATED
