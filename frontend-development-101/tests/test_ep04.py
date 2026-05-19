from __future__ import annotations

from conftest import load_module


def test_ep04_behavior() -> None:
    mod = load_module("ko/04-components-and-state/step01_ep04.py", "ep04")
    rendered = mod.run_demo()
    assert rendered == "count=1 step=1"
