"""Api Design 101 - Episode 6: pagination and filtering example."""

from __future__ import annotations

from common import decode_cursor, encode_cursor
from fastapi import FastAPI, Query

ITEMS = [
    {"id": i, "status": "paid" if i % 2 == 0 else "pending"} for i in range(1, 101)
]


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/orders")
    def list_orders(
        limit: int = Query(default=20, ge=1, le=100),
        cursor: str | None = Query(default=None),
        status: str | None = Query(default=None),
    ) -> dict[str, object]:
        """List orders."""
        filtered = (
            ITEMS if status is None else [i for i in ITEMS if i["status"] == status]
        )
        start = decode_cursor(cursor)
        page = filtered[start : start + limit]
        next_pos = start + len(page)
        next_cursor = encode_cursor(next_pos) if next_pos < len(filtered) else None
        return {"items": page, "next_cursor": next_cursor}

    return app
