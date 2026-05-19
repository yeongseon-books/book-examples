from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


def build_app() -> FastAPI:
    app = FastAPI(title="API Design 101 Demo", version="1.0.0")

    @app.get("/users/{uid}", response_model=User)
    def get_user(uid: int) -> User:
        return User(id=uid, name="yeongseon")

    return app
