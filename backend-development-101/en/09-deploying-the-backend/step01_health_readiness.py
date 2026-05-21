"""Backend Development 101 - Episode 9: deploying the backend example."""

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
