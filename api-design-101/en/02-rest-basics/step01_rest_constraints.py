from __future__ import annotations

from fastapi import FastAPI


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/users/{uid}")
    def get_user(uid: int) -> dict[str, int | str]:
        return {"id": uid, "name": "yeongseon"}

    @app.post("/users", status_code=201)
    def create_user() -> tuple[dict[str, int], int]:
        return {"id": 43}, 201

    return app
