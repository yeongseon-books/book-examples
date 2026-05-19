from __future__ import annotations

from conftest import load_module


def test_ep09_behavior() -> None:
    mod = load_module("ko/09-build-tools-and-bundling/step01_ep09.py", "ep09")
    sizes = mod.run_demo()
    assert sizes["min"] <= sizes["raw"]
