class UserRepository:
    def __init__(self) -> None:
        self._users: dict[str, dict] = {}

    def save(self, user_id: str, name: str) -> None:
        self._users[user_id] = {"id": user_id, "name": name}

    def get(self, user_id: str) -> dict | None:
        return self._users.get(user_id)


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register(self, user_id: str, name: str) -> None:
        if not name.strip():
            raise ValueError("name required")
        self.repo.save(user_id, name)


class UserController:
    def __init__(self, service: UserService) -> None:
        self.service = service

    def create_user(self, payload: dict) -> str:
        self.service.register(payload["id"], payload["name"])
        return "created"
