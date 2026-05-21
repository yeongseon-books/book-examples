"""Api Design 101 - 1편: what is an api 예제."""

from __future__ import annotations

from fastapi import FastAPI


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/health")
    def health() -> dict[str, str]:
        """Health."""
        return {"status": "ok"}

    return app
