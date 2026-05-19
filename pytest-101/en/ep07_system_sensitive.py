"""Pytest 101 - Episode 7: System sensitive."""

import datetime
from pathlib import Path


def write_daily_note(base_dir: Path, text: str) -> Path:
    """Write daily note."""
    env = __import__("os").environ.get("APP_ENV", "dev")
    date_part = datetime.date.today().isoformat()
    target = base_dir / f"{env}-{date_part}.txt"
    target.write_text(text, encoding="utf-8")
    return target
