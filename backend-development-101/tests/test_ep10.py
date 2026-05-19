"""Tests for ep10 in Backend Development 101."""

from conftest import load_module
from fastapi.testclient import TestClient


def test_ep10_cache_queue_metrics() -> None:
    """Test ep10 cache queue metrics."""
    app = load_module(
        "ko/10-production-ready-backend/step01_production_architecture.py", "ep10"
    ).build_app()
    client = TestClient(app)
    first = client.post("/tasks/T-1").json()
    second = client.post("/tasks/T-1").json()
    metrics = client.get("/ops/metrics").json()
    assert first["source"] == "queue"
    assert second["source"] == "cache"
    assert metrics["queued_jobs"] == 1
