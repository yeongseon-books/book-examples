"""Episode 01: Minimal backend responsibility example."""

from fastapi import FastAPI


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/")
    def root() -> dict[str, str]:
        """Root."""
        return {"message": "hello backend"}

    @app.get("/health")
    def health() -> dict[str, str]:
        """Health."""
        return {"status": "ok"}

    return app
