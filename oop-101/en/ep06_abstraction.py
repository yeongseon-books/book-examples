from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self, user_id: str, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: str) -> str | None:
        raise NotImplementedError


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def save(self, user_id: str, name: str) -> None:
        self._data[user_id] = name

    def get(self, user_id: str) -> str | None:
        return self._data.get(user_id)


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register(self, user_id: str, name: str) -> None:
        self.repo.save(user_id, name)


if __name__ == "__main__":
    repo = InMemoryUserRepository()
    service = UserService(repo)
    service.register("u1", "mina")
    print(repo.get("u1"))
