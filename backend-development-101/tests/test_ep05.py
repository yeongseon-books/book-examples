from conftest import load_module
from fastapi.testclient import TestClient


def test_ep05_sqlite_repository_flow() -> None:
    app = load_module(
        "ko/05-database-layer/step01_repository_sqlite.py", "ep05"
    ).build_app()
    client = TestClient(app)
    client.post("/users", json={"name": "Alice"})
    client.post("/users", json={"name": "Bob"})
    users = client.get("/users").json()["users"]
    assert users == ["Alice", "Bob"]
