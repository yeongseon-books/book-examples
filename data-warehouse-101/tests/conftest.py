"""Pytest configuration and fixtures for Data Warehouse 101."""

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_episode(lang, filename):
    """Load episode."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    return runpy.run_path(str(ROOT / lang / filename))
