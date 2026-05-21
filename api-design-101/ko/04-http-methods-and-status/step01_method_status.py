"""Api Design 101 - 4편: http methods and status 예제."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Response

USERS: dict[int, dict[str, int | str]] = {42: {"id": 42, "name": "Y"}}


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/users/{uid}")
    def get_user(uid: int) -> dict[str, int | str]:
        """Get user."""
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="not found")
        return USERS[uid]

    @app.delete("/users/{uid}", status_code=204)
    def delete_user(uid: int) -> Response:
        """Delete user."""
        USERS.pop(uid, None)
        return Response(status_code=204)

    return app
