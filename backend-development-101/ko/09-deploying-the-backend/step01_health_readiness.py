"""에피소드 09: 배포를 위한 health/readiness 및 환경 설정 예제입니다."""

import os

from fastapi import FastAPI


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    app.state.env = os.environ.get("APP_ENV", "dev")

    @app.get("/healthz")
    def healthz():
        """Healthz."""
        return {"status": "ok"}

    @app.get("/readyz")
    def readyz():
        """Readyz."""
        ready = app.state.env in {"dev", "staging", "prod"}
        return {"ready": ready, "env": app.state.env}

    return app
