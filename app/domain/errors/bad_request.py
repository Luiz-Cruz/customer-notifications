from app.domain.http.status_code import HttpStatusCode
from app.domain.errors.api_exception import ApiException


class BadRequest(ApiException):
    def __init__(self, error_msg: str):
        super().__init__(error_msg, HttpStatusCode.BAD_REQUEST)
