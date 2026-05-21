"""Api Design 101 - Episode 9: api versioning example."""

from __future__ import annotations

from fastapi import FastAPI, Response


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.get("/v1/users/{uid}")
    def v1(uid: int, response: Response) -> dict[str, int | str]:
        """V1."""
        response.headers["Deprecation"] = "true"
        response.headers["Sunset"] = "Wed, 31 Jan 2027 23:59:59 GMT"
        response.headers["Link"] = '</v2/users/{id}; rel="successor-version"'
        return {"id": uid, "name": "Y"}

    @app.get("/v2/users/{uid}")
    def v2(uid: int) -> dict[str, int | str]:
        """V2."""
        return {"id": uid, "full_name": "Yeongseon", "username": "y"}

    return app
