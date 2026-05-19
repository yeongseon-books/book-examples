"""Tests for ep08 in Web Development 101."""

from en.ep08_deployment import app_factory, gunicorn_fixture_text, readiness_check


def test_ep08_readiness_and_health(monkeypatch):
    """Test ep08 readiness and health."""
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("CI", "true")
    assert readiness_check()["port_set"] is True
    assert "workers" in gunicorn_fixture_text()
    app = app_factory()
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["port"] == "8000"
