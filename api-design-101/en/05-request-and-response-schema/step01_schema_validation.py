from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field


class CreateUserIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str = Field(min_length=3, max_length=32)
    email: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str


def build_app() -> FastAPI:
    app = FastAPI()

    @app.post("/users", response_model=UserOut, status_code=201)
    def create_user(payload: CreateUserIn) -> UserOut:
        return UserOut(id=100, username=payload.username, email=payload.email)

    return app
