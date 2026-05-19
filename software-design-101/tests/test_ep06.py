"""Tests for ep06 in Software Design 101."""

from ko.ep06_layered_architecture import UserController, UserRepository, UserService


def test_ep06_layered_flow() -> None:
    """Test ep06 layered flow."""
    repo = UserRepository()
    service = UserService(repo)
    controller = UserController(service)
    assert controller.create_user({"id": "u1", "name": "Kim"}) == "created"
    assert repo.get("u1") == {"id": "u1", "name": "Kim"}
