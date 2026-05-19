"""Shared helpers for python-101 demos."""

from __future__ import annotations


def print_banner(title: str) -> str:
    """Print banner."""
    line = f"=== {title} ==="
    print(line)
    return line
