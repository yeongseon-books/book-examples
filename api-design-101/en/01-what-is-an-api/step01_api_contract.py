"""Api Design 101 - Episode 1: what is an api example."""

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
