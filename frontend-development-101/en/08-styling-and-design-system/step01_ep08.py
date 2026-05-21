"""Frontend Development 101 - Episode 8: styling and design system example."""

from __future__ import annotations

from common import DesignTokenChecker

TOKENS = (
    '{"color.primary": "#1d72ff", "spacing.gutter": "1rem", "font.body": "Pretendard"}'
)


def run_demo() -> list[str]:
    """Run demo."""
    checker = DesignTokenChecker(TOKENS)
    return checker.require_keys(["color.primary", "spacing.gutter", "font.body"])
