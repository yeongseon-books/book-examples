"""Pytest 101 - Episode 4: Db like."""


class InMemoryUserDB:
    """In memory user d b."""

    def __init__(self) -> None:
        self._users: dict[int, str] = {}

    def add_user(self, user_id: int, name: str) -> None:
        """Add user."""
        self._users[user_id] = name

    def get_user(self, user_id: int) -> str | None:
        """Get user."""
        return self._users.get(user_id)

    def clear(self) -> None:
        """Clear."""
        self._users.clear()
