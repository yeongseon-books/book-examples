"""Episode 01: Minimal backend responsibility example."""

from fastapi import FastAPI


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    def root() -> dict[str, str]:
        return {"message": "hello backend"}

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
