from __future__ import annotations

from conftest import load_module


def test_ep01_behavior() -> None:
    mod = load_module("ko/01-what-is-frontend-development/step01_ep01.py", "ep01")
    result = mod.run_demo()
    assert result["semantic_ok"] is True
    assert result["missing_alt"] == 0
