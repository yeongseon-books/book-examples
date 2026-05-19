"""Tests for ep06 in Oop 101."""

from ko.ep06_abstraction import InMemoryUserRepository, UserService


def test_ep06_repository_abstraction() -> None:
    """Test ep06 repository abstraction."""
    repo = InMemoryUserRepository()
    service = UserService(repo)
    service.register("u42", "hana")
    assert repo.get("u42") == "hana"
