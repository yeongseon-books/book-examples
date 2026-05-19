"""Tests for ep03 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module("ko/03-defining-the-problem/step01_problem_card.py", "ko_ep03").run,
)
en_run = cast(
    "Runner",
    load_module("en/03-defining-the-problem/step01_problem_card.py", "en_ep03").run,
)


def test_ep03_ko_behavior() -> None:
    """Test ep03 ko behavior."""
    assert "30" in str(ko_run()["metric"])


def test_ep03_en_behavior() -> None:
    """Test ep03 en behavior."""
    assert "30" in str(en_run()["metric"])
