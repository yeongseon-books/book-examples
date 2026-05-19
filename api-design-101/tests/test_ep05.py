from __future__ import annotations

from .helpers import client_for, load_module


def test_ep05_schema_validation() -> None:
    mod = load_module(
        "ko/05-request-and-response-schema/step01_schema_validation.py", "ep05_ko"
    )
    app = mod.build_app()
    c = client_for(app)
    ok = c.post("/users", json={"username": "user01", "email": "u@example.com"})
    bad = c.post(
        "/users", json={"username": "ab", "email": "u@example.com", "extra": "x"}
    )
    assert ok.status_code == 201
    assert bad.status_code == 422
