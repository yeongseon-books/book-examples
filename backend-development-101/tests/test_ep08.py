"""Tests for ep08 in Backend Development 101."""

from conftest import load_module
from fastapi.testclient import TestClient


def test_ep08_dependency_override_for_tests() -> None:
    """Test ep08 dependency override for tests."""
    module = load_module("ko/08-testing-the-backend/step01_testable_app.py", "ep08")
    app = module.build_app()
    sink = module.Sink()
    app.dependency_overrides[module.get_sink] = lambda: sink
    client = TestClient(app)
    r = client.post("/messages", json={"text": "hello"})
    assert r.status_code == 200
    assert sink.events == ["message:hello"]
