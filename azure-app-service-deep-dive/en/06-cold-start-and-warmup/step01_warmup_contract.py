from __future__ import annotations

from common import warmup_is_ready
from fastapi import FastAPI, Response


def create_app(is_ready: bool) -> FastAPI:
    app = FastAPI()

    @app.get("/warmup")
    def warmup(response: Response) -> dict[str, str]:
        # Return 503 until warmup is complete.
        if is_ready:
            return {"status": "ready"}
        response.status_code = 503
        return {"status": "warming"}

    return app


def check_ready(status_code: int, statuses: set[int]) -> bool:
    return warmup_is_ready(status_code, statuses)
