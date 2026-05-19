"""Software Design 101 - Episode 6: Layered architecture."""


class UserRepository:
    """User repository."""

    def __init__(self) -> None:
        self._users: dict[str, dict] = {}

    def save(self, user_id: str, name: str) -> None:
        """Save."""
        self._users[user_id] = {"id": user_id, "name": name}

    def get(self, user_id: str) -> dict | None:
        """Get."""
        return self._users.get(user_id)


class UserService:
    """User service."""

    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register(self, user_id: str, name: str) -> None:
        """Register."""
        if not name.strip():
            raise ValueError("name required")
        self.repo.save(user_id, name)


class UserController:
    """User controller."""

    def __init__(self, service: UserService) -> None:
        self.service = service

    def create_user(self, payload: dict) -> str:
        """Create user."""
        self.service.register(payload["id"], payload["name"])
        return "created"
