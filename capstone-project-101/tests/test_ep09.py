"""Tests for ep09 in Capstone Project 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(
    "Runner",
    load_module(
        "ko/09-presentation-materials/step01_presentation_flow.py", "ko_ep09"
    ).run,
)
en_run = cast(
    "Runner",
    load_module(
        "en/09-presentation-materials/step01_presentation_flow.py", "en_ep09"
    ).run,
)


def test_ep09_ko_behavior() -> None:
    """Test ep09 ko behavior."""
    assert ko_run()["minutes"] == {"talk": 8, "demo": 5, "qna": 7}


def test_ep09_en_behavior() -> None:
    """Test ep09 en behavior."""
    assert en_run()["minutes"] == {"talk": 8, "demo": 5, "qna": 7}
