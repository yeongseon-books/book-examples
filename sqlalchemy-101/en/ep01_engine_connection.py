"""Sqlalchemy 101 - Episode 1: Engine connection."""

from common import sync_engine
from sqlalchemy import text


def run() -> int:
    """Run."""
    engine = sync_engine()
    with engine.connect() as conn:
        value = conn.execute(text("select 1")).scalar_one()
    return int(value)
