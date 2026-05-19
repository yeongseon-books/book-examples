"""Testing 101 - Episode 3: Integration test."""


class UserRepository:
    """User repository."""

    def __init__(self, conn):
        self.conn = conn

    def add_user(self, user_id: int, name: str) -> None:
        """Add user."""
        self.conn.execute(
            "INSERT INTO users(user_id, name) VALUES (?, ?)", (user_id, name)
        )
        self.conn.commit()


class NameValidator:
    """Name validator."""

    def is_valid(self, name: str) -> bool:
        """Is valid."""
        return isinstance(name, str) and len(name.strip()) >= 2


class UserService:
    """User service."""

    def __init__(self, repo: UserRepository, validator: NameValidator):
        self.repo = repo
        self.validator = validator

    def register(self, user_id: int, name: str) -> bool:
        """Register."""
        if not self.validator.is_valid(name):
            return False
        self.repo.add_user(user_id, name.strip())
        return True
