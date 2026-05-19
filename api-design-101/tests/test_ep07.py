from __future__ import annotations

from .helpers import client_for, load_module


def test_ep07_problem_json_envelope() -> None:
    mod = load_module("ko/07-error-response-design/step01_problem_json.py", "ep07_ko")
    app = mod.build_app()
    res = client_for(app).get("/users/42")
    assert res.status_code == 404
    assert res.headers["content-type"].startswith("application/problem+json")
    assert res.json()["code"] == "user.not_found"
