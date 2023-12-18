from flask import Blueprint

ping_router = Blueprint("ping", __name__)


@ping_router.route("/ping")
def ping():
    return "pong"
