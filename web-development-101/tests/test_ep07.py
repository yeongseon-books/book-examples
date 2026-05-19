"""Tests for ep07 in Web Development 101."""

from pathlib import Path

from en.ep07_db_connection import run


def test_ep07_sqlite_crud(tmp_path):
    """Test ep07 sqlite crud."""
    db_path = str(Path(tmp_path) / "ep07.db")
    app = run(db_path)
    c = app.test_client()
    created = c.post("/users", json={"name": "kim"})
    assert created.status_code == 201
    users = c.get("/users").get_json()
    assert len(users) == 1
    assert users[0]["name"] == "kim"
