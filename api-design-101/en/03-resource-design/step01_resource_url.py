"""Api Design 101 - Episode 1: Resource url."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException

USERS = {42: {"id": 42, "name": "yeongseon"}}
ORDERS = {(42, 9): {"id": 9, "user_id": 42, "status": "paid"}}


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/users/{uid}")
    def user(uid: int) -> dict[str, int | str]:
        """User."""
        if uid not in USERS:
            raise HTTPException(status_code=404, detail="not found")
        return USERS[uid]

    @app.get("/users/{uid}/orders/{oid}")
    def user_order(uid: int, oid: int) -> dict[str, int | str]:
        """User order."""
        key = (uid, oid)
        if key not in ORDERS:
            raise HTTPException(status_code=404, detail="not found")
        return ORDERS[key]

    return app
