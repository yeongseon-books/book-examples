"""Tests for ep02 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module("ko/02-choosing-a-topic/step01_topic_matrix.py", "ko_ep02").run,
)
en_run = cast(
    "Runner",
    load_module("en/02-choosing-a-topic/step01_topic_matrix.py", "en_ep02").run,
)


def test_ep02_ko_behavior() -> None:
    """Test ep02 ko behavior."""
    assert ko_run()["pick"] == "schedule_checker"


def test_ep02_en_behavior() -> None:
    """Test ep02 en behavior."""
    assert en_run()["pick"] == "schedule_checker"
