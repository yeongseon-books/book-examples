"""Tests for ep05 in Web Development 101."""

from en.ep05_frontend_backend import run


def test_ep05_api_contract():
    """Test ep05 api contract."""
    app = run()
    c = app.test_client()
    r = c.get("/api/data")
    data = r.get_json()
    assert r.status_code == 200
    assert set(data.keys()) == {"message", "version"}
