from __future__ import annotations

from .helpers import client_for
from .helpers import load_module


def test_ep09_versioning_headers() -> None:
    mod = load_module("ko/09-api-versioning/step01_versioning_strategy.py", "ep09_ko")
    app = mod.build_app()
    c = client_for(app)
    v1 = c.get("/v1/users/42")
    v2 = c.get("/v2/users/42")
    assert v1.headers["deprecation"] == "true"
    assert "full_name" in v2.json()
