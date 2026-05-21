"""Api Design 101 - Episode 8: openapi and swagger example."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    """User."""

    id: int
    name: str


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI(title="API Design 101 Demo", version="1.0.0")

    @app.get("/users/{uid}", response_model=User)
    def get_user(uid: int) -> User:
        """Get user."""
        return User(id=uid, name="yeongseon")

    return app
