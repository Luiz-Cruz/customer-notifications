from app.domain.http.status_code import HttpStatusCode
from app.domain.errors.api_exception import ApiException


class BadRequest(ApiException):
    def __init__(self, error_msg: str):
        key = 'ex.generic.bad-request'
        super().__init__(HttpStatusCode.BAD_REQUEST, key, error_msg)
