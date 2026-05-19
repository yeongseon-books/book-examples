"""Episode 04: Business rules in a service layer."""

from collections.abc import Mapping
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


@dataclass
class UserRepo:
    """User repo."""

    users: list[Mapping[str, object]]

    def insert(self, name: str, age: int) -> Mapping[str, object]:
        """Insert."""
        user = {"id": len(self.users) + 1, "name": name, "age": age}
        self.users.append(user)
        return user


class RegisterIn(BaseModel):
    """Register in."""

    name: str
    age: int


class UserService:
    """User service."""

    def __init__(self, repo: UserRepo):
        self.repo = repo

    def register(self, payload: RegisterIn) -> Mapping[str, object]:
        """Register."""
        if payload.age < 14:
            raise ValueError("age must be >= 14")
        return self.repo.insert(payload.name, payload.age)


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    repo = UserRepo(users=[])
    service = UserService(repo=repo)

    @app.post("/register")
    def register(payload: RegisterIn):
        """Register."""
        try:
            return service.register(payload)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    return app
