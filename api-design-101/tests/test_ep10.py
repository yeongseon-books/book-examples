from __future__ import annotations

from .helpers import client_for
from .helpers import load_module


def test_ep10_docs_entrypoint() -> None:
    mod = load_module("ko/10-writing-good-api-docs/step01_docs_quality.py", "ep10_ko")
    app = mod.build_app()
    c = client_for(app)
    assert c.get("/health").status_code == 200
    assert c.get("/openapi.json").status_code == 200
