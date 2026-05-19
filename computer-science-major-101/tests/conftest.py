"""Pytest configuration and fixtures for Computer Science Major 101."""

import importlib.util
from pathlib import Path
from types import ModuleType


def load_module(relative_path: str) -> ModuleType:
    """Load module."""
    root = Path(__file__).resolve().parents[1]
    path = root / relative_path
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
