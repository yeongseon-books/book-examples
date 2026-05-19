from __future__ import annotations

from fastapi import FastAPI


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
