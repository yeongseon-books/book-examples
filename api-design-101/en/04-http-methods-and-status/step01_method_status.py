from __future__ import annotations

from fastapi import FastAPI, HTTPException, Response

USERS: dict[int, dict[str, int | str]] = {42: {"id": 42, "name": "Y"}}


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/users/{uid}")
    def get_user(uid: int) -> dict[str, int | str]:
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="not found")
        return USERS[uid]

    @app.delete("/users/{uid}", status_code=204)
    def delete_user(uid: int) -> Response:
        USERS.pop(uid, None)
        return Response(status_code=204)

    return app
