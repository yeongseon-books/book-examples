"""Alembic 101 - Episode 1: Team workflow."""

from __future__ import annotations


def ci_checks() -> list[str]:
    """Ci checks."""
    return [
        "pytest",
        "alembic check",
        "upgrade->downgrade->upgrade",
        "sql preview",
        "single head guard",
    ]


def health_payload(current: str, expected: str) -> dict[str, str]:
    """Health payload."""
    return {
        "status": "ok" if current == expected else "drift",
        "alembic_version": current,
        "expected": expected,
    }


if __name__ == "__main__":
    print(health_payload("abc", "abc"))
