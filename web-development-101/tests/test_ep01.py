"""Tests for ep01 in Web Development 101."""

from en.ep01_http_request_response import run


def test_ep01_http_request_response():
    """Test ep01 http request response."""
    app = run()
    c = app.test_client()
    r = c.get("/inspect", headers={"User-Agent": "pytest"})
    data = r.get_json()
    assert r.status_code == 200
    assert data["method"] == "GET"
    assert data["path"] == "/inspect"
    assert data["status"] == 200
