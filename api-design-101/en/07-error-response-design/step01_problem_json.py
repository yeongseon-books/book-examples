from __future__ import annotations

from common import problem
from fastapi import FastAPI
from fastapi.responses import JSONResponse


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/users/{uid}")
    def get_user(uid: int) -> JSONResponse:
        body = problem(
            404, "user.not_found", "User not found", f"User {uid} does not exist."
        )
        return JSONResponse(
            body, status_code=404, media_type="application/problem+json"
        )

    return app
