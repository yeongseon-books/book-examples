"""Tests for ep06 in Web Development 101."""

from en.ep06_auth_sessions import run


def test_ep06_auth_session_flow():
    """Test ep06 auth session flow."""
    app = run()
    c = app.test_client()
    assert c.get("/protected").status_code == 401
    ok = c.post("/login", json={"username": "alice", "password": "pw123"})
    assert ok.status_code == 200
    assert c.get("/protected").status_code == 200
    assert c.post("/logout").status_code == 200
