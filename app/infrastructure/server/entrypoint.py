from flask import Flask

from app.infrastructure.server import url_mapping


def start():
    """
    Starts the application

    Returns:
        Flask: Flask application
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    url_mapping.map_routes(app)
    app.app_context().push()
    return app
