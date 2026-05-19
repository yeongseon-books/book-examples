"""Oop 101 - Episode 6: Abstraction."""

from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self, user_id: str, name: str) -> None:
        """Save."""
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: str) -> str | None:
        """Get."""
        raise NotImplementedError


class InMemoryUserRepository(UserRepository):
    """In memory user repository."""

    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def save(self, user_id: str, name: str) -> None:
        """Save."""
        self._data[user_id] = name

    def get(self, user_id: str) -> str | None:
        """Get."""
        return self._data.get(user_id)


class UserService:
    """User service."""

    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register(self, user_id: str, name: str) -> None:
        """Register."""
        self.repo.save(user_id, name)


if __name__ == "__main__":
    repo = InMemoryUserRepository()
    service = UserService(repo)
    service.register("u1", "mina")
    print(repo.get("u1"))
