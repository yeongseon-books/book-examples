"""Pytest configuration and fixtures for Harness Engineering 101."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_episode(lang: str, slug: str):
    """Load episode."""
    path = ROOT / lang / slug / "step01_example.py"
    spec = importlib.util.spec_from_file_location(f"{lang}_{slug}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load episode module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
