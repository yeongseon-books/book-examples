"""Clean Code 101 - Episode 1: Testable code."""

from dataclasses import dataclass
from datetime import datetime


def is_overdue(due: datetime, now: datetime | None = None) -> bool:
    """Is overdue."""
    current = now or datetime.now()
    return current > due


@dataclass
class FakeRepo:
    """Fake repo."""

    users: dict[str, dict]

    def __init__(self) -> None:
        self.users = {}

    def save(self, user: dict) -> None:
        """Save."""
        self.users[user["id"]] = user

    def get(self, user_id: str) -> dict | None:
        """Get."""
        return self.users.get(user_id)


def register(repo: FakeRepo, user: dict) -> dict:
    """Register."""
    repo.save(user)
    return user
