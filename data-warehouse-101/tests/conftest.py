"""Pytest configuration and fixtures for Data Warehouse 101."""

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_episode(lang, filename):
    """Load episode."""
    return runpy.run_path(str(ROOT / lang / filename))
