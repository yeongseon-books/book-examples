"""Tests for ep05 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module("ko/05-splitting-team-roles/step01_role_split.py", "ko_ep05").run,
)
en_run = cast(
    "Runner",
    load_module("en/05-splitting-team-roles/step01_role_split.py", "en_ep05").run,
)


def test_ep05_ko_behavior() -> None:
    """Test ep05 ko behavior."""
    assert ko_run()["review"] == "weekly"


def test_ep05_en_behavior() -> None:
    """Test ep05 en behavior."""
    assert en_run()["review"] == "weekly"
