from fastapi.testclient import TestClient

from conftest import load_module


def test_ep02_status_header_and_validation() -> None:
    app = load_module("ko/02-building-an-http-server/step01_status_headers.py", "ep02").build_app()
    client = TestClient(app)
    ok = client.get("/items/2")
    bad = client.get("/items/-1")
    assert ok.status_code == 200
    assert ok.headers["X-App"] == "backend-101"
    assert bad.status_code == 400
