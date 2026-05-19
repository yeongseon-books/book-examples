"""Azure Aca Deep Dive - Episode 1: Ingress path."""

from __future__ import annotations

from common import as_json
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient


def create_app() -> FastAPI:
    """Create app."""
    app = FastAPI()

    @app.get("/ingress")
    def ingress(request: Request) -> dict[str, object]:
        """Ingress."""
        proto = request.headers.get("x-forwarded-proto", "http")
        canary = request.headers.get("x-canary", "off")
        revision = "orders--green" if canary == "on" else "orders--blue"
        return {"proto": proto, "revision": revision, "tls_terminated_at": "ingress"}

    return app


def run() -> dict[str, object]:
    """Run."""
    app = create_app()
    client = TestClient(app)
    response = client.get(
        "/ingress", headers={"x-forwarded-proto": "https", "x-canary": "on"}
    )
    return {
        "episode": 6,
        "result": response.json(),
        "status_code": response.status_code,
    }


if __name__ == "__main__":
    print(as_json(run()))
