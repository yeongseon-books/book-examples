"""Tests for ep10 in Web Development 101."""

from pathlib import Path

from en.ep10_small_web_app import run


def test_ep10_todo_app_auth_and_rest(tmp_path):
    """Test ep10 todo app auth and rest."""
    db_path = str(Path(tmp_path) / "ep10.db")
    app = run(db_path)
    c = app.test_client()
    assert c.get("/api/v1/todos").status_code == 401
    assert (
        c.post("/login", json={"username": "alice", "password": "pw123"}).status_code
        == 200
    )
    created = c.post("/api/v1/todos", json={"title": "write tests"})
    assert created.status_code == 201
    listed = c.get("/api/v1/todos")
    data = listed.get_json()
    assert listed.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "write tests"
