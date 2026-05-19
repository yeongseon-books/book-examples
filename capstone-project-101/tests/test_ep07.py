"""Tests for ep07 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module(
        "ko/07-choosing-the-tech-stack/step01_stack_decision.py", "ko_ep07"
    ).run,
)
en_run = cast(
    "Runner",
    load_module(
        "en/07-choosing-the-tech-stack/step01_stack_decision.py", "en_ep07"
    ).run,
)


def test_ep07_ko_behavior() -> None:
    """Test ep07 ko behavior."""
    assert ko_run()["pick"] == "Flask"


def test_ep07_en_behavior() -> None:
    """Test ep07 en behavior."""
    assert en_run()["pick"] == "Flask"
