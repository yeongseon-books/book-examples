"""Shared utilities and domain models for Database Systems 101."""

from __future__ import annotations

import sqlite3
from collections import namedtuple
from pathlib import Path

Row = namedtuple("Row", ["id", "value"])


def make_db(path: str = ":memory:") -> sqlite3.Connection:
    """Make db."""
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def reset_file(path: str) -> None:
    """Reset file."""
    p = Path(path)
    if p.exists():
        p.unlink()
