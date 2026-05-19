"""Episode 04: Business rules in a service layer."""

from dataclasses import dataclass
from typing import Mapping

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


@dataclass
class UserRepo:
    users: list[Mapping[str, object]]

    def insert(self, name: str, age: int) -> Mapping[str, object]:
        user = {"id": len(self.users) + 1, "name": name, "age": age}
        self.users.append(user)
        return user


class RegisterIn(BaseModel):
    name: str
    age: int


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def register(self, payload: RegisterIn) -> Mapping[str, object]:
        if payload.age < 14:
            raise ValueError("age must be >= 14")
        return self.repo.insert(payload.name, payload.age)


def build_app() -> FastAPI:
    app = FastAPI()
    repo = UserRepo(users=[])
    service = UserService(repo=repo)

    @app.post("/register")
    def register(payload: RegisterIn):
        try:
            return service.register(payload)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    return app
