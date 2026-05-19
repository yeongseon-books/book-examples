"""에피소드 01: 백엔드의 최소 책임(요청/응답) 예제입니다."""

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
