"""Api Design 101 - Episode 1: Rest constraints."""

from __future__ import annotations

from fastapi import FastAPI


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/users/{uid}")
    def get_user(uid: int) -> dict[str, int | str]:
        """Get user."""
        return {"id": uid, "name": "yeongseon"}

    @app.post("/users", status_code=201)
    def create_user(
        payload: dict[str, object] | None = None,
    ) -> tuple[dict[str, int], int]:
        """Create user."""
        if payload is not None and "name" not in payload:
            raise ValueError("missing required field: name")
        return {"id": 43}, 201

    return app
