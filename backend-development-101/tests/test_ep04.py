from fastapi.testclient import TestClient

from conftest import load_module


def test_ep04_service_business_rule() -> None:
    app = load_module("ko/04-service-layer/step01_service_layer.py", "ep04").build_app()
    client = TestClient(app)
    assert client.post("/register", json={"name": "Kim", "age": 20}).status_code == 200
    assert client.post("/register", json={"name": "Min", "age": 10}).status_code == 400
