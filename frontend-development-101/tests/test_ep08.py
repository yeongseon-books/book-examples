from __future__ import annotations

from conftest import load_module


def test_ep08_behavior() -> None:
    mod = load_module("ko/08-styling-and-design-system/step01_ep08.py", "ep08")
    missing = mod.run_demo()
    assert missing == []
