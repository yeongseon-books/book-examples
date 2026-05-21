"""Frontend Development 101 - 8편: styling and design system 예제."""

from __future__ import annotations

from common import DesignTokenChecker

TOKENS = (
    '{"color.primary": "#1d72ff", "spacing.gutter": "1rem", "font.body": "Pretendard"}'
)


def run_demo() -> list[str]:
    """데모를 실행합니다."""
    checker = DesignTokenChecker(TOKENS)
    return checker.require_keys(["color.primary", "spacing.gutter", "font.body"])
