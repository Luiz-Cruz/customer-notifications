from app.adapters.http.http_response_adapter import respond_api_error


def test_respond_api_error():
    response = respond_api_error("error_details", 400)
    assert response.status_code == 400
    assert response.mimetype == "application/json"
    assert response.data == b'{"message": "error_details", "status": 400}'
    