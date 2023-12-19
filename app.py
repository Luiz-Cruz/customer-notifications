from app import create_app
from app.domain.errors.api_exception import ApiException
from app.domain.errors.bad_request import BadRequest
from app.domain.errors.error_handler import handle_exception

app = create_app()
app.register_error_handler(BadRequest, handle_exception)
app.register_error_handler(ApiException, handle_exception)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    app.register_error_handler()
