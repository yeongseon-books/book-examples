"""Episode 09: Deployment-oriented health/readiness configuration."""

import os

from fastapi import FastAPI


def build_app() -> FastAPI:
    app = FastAPI()
    app.state.env = os.environ.get("APP_ENV", "dev")

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    @app.get("/readyz")
    def readyz():
        ready = app.state.env in {"dev", "staging", "prod"}
        return {"ready": ready, "env": app.state.env}

    return app
