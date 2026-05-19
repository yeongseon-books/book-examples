"""Azure App Service 101 - Episode 1: Offline deploy demo."""

from __future__ import annotations

# pyright: reportUnusedFunction=false
import os

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create app."""
    app = FastAPI()

    @app.get("/")
    def root() -> dict[str, str]:
        """Root."""
        return {
            "message": "Hello from Azure App Service",
            "environment": os.getenv("APP_ENV", "development"),
        }

    @app.get("/health")
    def health() -> dict[str, str]:
        """Health."""
        return {"status": "healthy"}

    return app


def build_startup_command() -> str:
    """Build startup command."""
    return "gunicorn --bind=0.0.0.0:$PORT src.app:app"
