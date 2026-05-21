"""Api Design 101 - Episode 10: writing good api docs example."""

from __future__ import annotations

from fastapi import FastAPI


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI(
        title="API Design 101 Demo",
        version="1.0.0",
        summary="Getting Started in 5 minutes",
        description="Includes examples, changelog-ready endpoints, and OpenAPI docs.",
    )

    @app.get("/health", summary="Health check", tags=["getting-started"])
    def health() -> dict[str, str]:
        """Health."""
        return {"status": "ok"}

    return app
