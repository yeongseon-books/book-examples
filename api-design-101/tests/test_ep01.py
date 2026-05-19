from __future__ import annotations

from .helpers import client_for, load_module


def test_ep01_health_contract() -> None:
    mod = load_module("ko/01-what-is-an-api/step01_api_contract.py", "ep01_ko")
    app = mod.build_app()
    res = client_for(app).get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
