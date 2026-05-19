"""Tests for ep03 in Backend Development 101."""

from conftest import load_module
from fastapi.testclient import TestClient


def test_ep03_router_and_params() -> None:
    """Test ep03 router and params."""
    app = load_module(
        "ko/03-routing-and-controllers/step01_routing_controller.py", "ep03"
    ).build_app()
    client = TestClient(app)
    assert client.get("/users", params={"active": "false", "limit": 5}).json() == {
        "active": False,
        "limit": 5,
    }
    created = client.post("/users", json={"name": "Alice", "active": True})
    assert created.status_code == 200
    assert created.json()["name"] == "Alice"
