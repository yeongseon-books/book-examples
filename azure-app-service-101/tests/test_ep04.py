from __future__ import annotations

from typing import Any, cast

from fastapi.testclient import TestClient

from conftest import load_module


def test_deploy_demo_app_health() -> None:
    mod = load_module("ko/04-first-deploy/step01_offline_deploy_demo.py", "ep04")
    create_app = cast(Any, mod.create_app)
    build_startup_command = cast(Any, mod.build_startup_command)
    app = create_app()
    client = TestClient(app)
    assert client.get("/health").json() == {"status": "healthy"}
    assert "$PORT" in build_startup_command()
