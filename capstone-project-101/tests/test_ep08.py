"""Tests for ep08 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module("ko/08-schedule-management/step01_schedule_plan.py", "ko_ep08").run,
)
en_run = cast(
    "Runner",
    load_module("en/08-schedule-management/step01_schedule_plan.py", "en_ep08").run,
)


def test_ep08_ko_behavior() -> None:
    """Test ep08 ko behavior."""
    assert ko_run()["progress"] == {"done": 12, "todo": 8, "blocked": 2}


def test_ep08_en_behavior() -> None:
    """Test ep08 en behavior."""
    assert en_run()["progress"] == {"done": 12, "todo": 8, "blocked": 2}


def test_ep08_buffer_enabled() -> None:
    """Test ep08 buffer enabled."""
    plan = ko_run()["plan"]
    assert plan.has_buffer() is True
