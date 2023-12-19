from flask import Response, Blueprint, jsonify
from loguru import logger

from app.presentation.models.notifications_body import NotificationsBody
from app.presentation.schemas.notifications import NotificationsSchema
from app.presentation.validation.notification_validator import validate_notifications_request


notifications_router = Blueprint("notifications_router", __name__)


@notifications_router.route("/notifications", methods=["POST"])
@validate_notifications_request(NotificationsSchema)
def create_notification(body: NotificationsBody) -> Response:
    """Creates a new customer notification"""
    logger.info(f"Creating notification: {body}")
    return jsonify({"message": "Notification received successfully"}), 201
