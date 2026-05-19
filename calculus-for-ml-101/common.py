"""Shared utilities and domain models for Calculus For Ml 101."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parent


def numerical_derivative_1d(func, x: float, h: float = 1e-5) -> float:
    """Numerical derivative 1d."""
    return (func(x + h) - func(x - h)) / (2 * h)


def numerical_partial(func, x: list[float], i: int, h: float = 1e-5) -> float:
    """Numerical partial."""
    xp = x.copy()
    xm = x.copy()
    xp[i] += h
    xm[i] -= h
    return (func(xp) - func(xm)) / (2 * h)


def load_module(relative_path: str) -> ModuleType:
    """Load module."""
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
