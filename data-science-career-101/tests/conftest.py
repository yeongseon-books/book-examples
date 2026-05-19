"""Pytest configuration and fixtures for Data Science Career 101."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(path: str):
    """Load module."""
    module_path = Path(path)
    spec = importlib.util.spec_from_file_location(
        module_path.stem.replace("-", "_"), module_path
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec.loader.exec_module(module)
    return module
