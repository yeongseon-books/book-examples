"""Alembic 101 - Episode 1: Branch merge."""

from __future__ import annotations


def merge_heads(left: str, right: str, merge_id: str = "m1") -> dict[str, object]:
    """Merge heads."""
    return {"revision": merge_id, "down_revisions": (left, right)}


def is_multi_head(heads: list[str]) -> bool:
    """Is multi head."""
    return len(heads) > 1


if __name__ == "__main__":
    print(merge_heads("a1", "b1"))
