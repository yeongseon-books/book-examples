"""Tests for ep09 in Backend Development 101."""

from conftest import load_module
from fastapi.testclient import TestClient


def test_ep09_health_and_readiness() -> None:
    """Test ep09 health and readiness."""
    app = load_module(
        "ko/09-deploying-the-backend/step01_health_readiness.py", "ep09"
    ).build_app()
    client = TestClient(app)
    assert client.get("/healthz").json() == {"status": "ok"}
    ready = client.get("/readyz").json()
    assert ready["ready"] is True
