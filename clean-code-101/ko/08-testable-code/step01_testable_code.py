from dataclasses import dataclass
from datetime import datetime


def is_overdue(due: datetime, now: datetime | None = None) -> bool:
    current = now or datetime.now()
    return current > due


@dataclass
class FakeRepo:
    users: dict[str, dict]

    def __init__(self) -> None:
        self.users = {}

    def save(self, user: dict) -> None:
        self.users[user["id"]] = user

    def get(self, user_id: str) -> dict | None:
        return self.users.get(user_id)


def register(repo: FakeRepo, user: dict) -> dict:
    repo.save(user)
    return user
