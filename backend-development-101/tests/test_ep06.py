"""Tests for ep06 in Backend Development 101."""

from conftest import load_module
from fastapi.testclient import TestClient


def test_ep06_auth_and_role_checks() -> None:
    """Test ep06 auth and role checks."""
    app = load_module(
        "ko/06-auth-and-authorization/step01_auth_roles.py", "ep06"
    ).build_app(secret="unit-secret")
    client = TestClient(app)
    token = client.post(
        "/login", json={"username": "admin", "password": "pw123"}
    ).json()["access_token"]
    assert (
        client.get("/me", headers={"Authorization": f"Bearer {token}"}).status_code
        == 200
    )
    assert (
        client.delete(
            "/admin/users/7", headers={"Authorization": f"Bearer {token}"}
        ).status_code
        == 200
    )
