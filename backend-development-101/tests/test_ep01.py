from conftest import load_module
from fastapi.testclient import TestClient


def test_ep01_ko_and_en_health() -> None:
    for locale in ("ko", "en"):
        app = load_module(
            f"{locale}/01-what-is-backend-development/step01_http_basics.py",
            f"ep01_{locale}",
        ).build_app()
        client = TestClient(app)
        assert client.get("/").json()["message"] == "hello backend"
        assert client.get("/health").json() == {"status": "ok"}
