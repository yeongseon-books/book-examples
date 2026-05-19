"""Azure App Service Deep Dive - Episode 1: Warmup contract."""

from __future__ import annotations

from common import warmup_is_ready
from fastapi import FastAPI, Response


def create_app(is_ready: bool) -> FastAPI:
    """Create app."""
    app = FastAPI()

    @app.get("/warmup")
    def warmup(response: Response) -> dict[str, str]:
        # 준비 완료 전에는 503으로 응답해 트래픽 진입을 막습니다.
        """Warmup."""
        if is_ready:
            return {"status": "ready"}
        response.status_code = 503
        return {"status": "warming"}

    return app


def check_ready(status_code: int, statuses: set[int]) -> bool:
    """Check ready."""
    return warmup_is_ready(status_code, statuses)
