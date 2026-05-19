from __future__ import annotations

from fastapi import FastAPI, Request


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/route")
    def route(request: Request) -> dict[str, str | bool]:
        cookie = request.headers.get("cookie", "")
        sticky = "ARRAffinity=" in cookie
        worker = "worker-2" if sticky else "worker-random"
        return {"sticky": sticky, "selected_worker": worker}

    return app
