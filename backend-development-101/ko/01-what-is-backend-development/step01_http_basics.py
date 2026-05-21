"""Backend Development 101 - 1편: what is backend development 예제."""

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
