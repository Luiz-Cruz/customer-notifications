from dataclasses import dataclass


@dataclass
class HttpStatusCode:
    """Dataclass representing the HTTP status codes raised by the API"""
    OK: int = 200
    CREATED: int = 201
    BAD_REQUEST: int = 400
    TOO_MANY_REQUESTS: int = 429
    INTERNAL_SERVER_ERROR: int = 500
    NOT_FOUND: int = 404
    FORBIDDEN: int = 403
