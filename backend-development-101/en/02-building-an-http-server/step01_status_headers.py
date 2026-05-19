"""Episode 02: HTTP server with status codes and headers."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


def build_app() -> FastAPI:
    app = FastAPI()

    @app.get("/items/{item_id}")
    def get_item(item_id: int):
        if item_id < 0:
            raise HTTPException(status_code=400, detail="item_id must be >= 0")
        return JSONResponse(content={"item_id": item_id}, headers={"X-App": "backend-101"})

    return app
