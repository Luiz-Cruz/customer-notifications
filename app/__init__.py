from flask import Flask

from app.infrastructure.server import url_mapping


def create_app():
    """
    Starts the application

    Returns:
        Flask: Flask application
    """

    app = Flask(__name__)
    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False
    url_mapping.map_routes(app)

    return app

