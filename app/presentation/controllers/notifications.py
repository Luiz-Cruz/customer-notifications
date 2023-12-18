from flask import Response, Blueprint, jsonify
from loguru import logger

from presentation.models.notifications_body import NotificationsBody
from presentation.schemas.notifications import NotificationsSchema
from presentation.validation.notificationsValidation import validate_notifications_request


notifications_router = Blueprint("notifications_router", __name__)


@notifications_router.route("/notifications", methods=["POST"])
@validate_notifications_request(NotificationsSchema)
def create_notification(body: NotificationsBody) -> Response:
    """Creates a new customer notification"""
    logger.info(f"Creating notification: {body}")
    return jsonify({"message": "Notification received successfully"}), 201
