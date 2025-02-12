from flask import Flask

from app.presentation.controllers.notifications_ctr import notifications_router
from app.presentation.controllers.ping_ctr import ping_router


def map_routes(application: Flask) -> None:
    """
    Map routes

    Args:
        application (Flask): Flask application
    """
    application.register_blueprint(ping_router)
    application.register_blueprint(notifications_router)
