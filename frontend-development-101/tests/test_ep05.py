from __future__ import annotations

from conftest import load_module


def test_ep05_behavior() -> None:
    mod = load_module("ko/05-routing-and-pages/step01_ep05.py", "ep05")
    ok, not_found = mod.run_demo()
    assert ok == "user:42"
    assert not_found == "404"
