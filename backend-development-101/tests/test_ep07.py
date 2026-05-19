from conftest import load_module
from fastapi.testclient import TestClient


def test_ep07_request_id_and_domain_error() -> None:
    app = load_module(
        "ko/07-logging-and-error-handling/step01_logging_errors.py", "ep07"
    ).build_app()
    client = TestClient(app)
    response = client.get("/orders/3", headers={"X-Request-ID": "rid-123"})
    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "rid-123"
    bad = client.get("/orders/0")
    assert bad.status_code == 400
    assert bad.json()["code"] == "INVALID_AMOUNT"
