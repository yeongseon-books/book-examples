"""Shared utilities and domain models for Type Hints Python 101."""

from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Project root."""
    return Path(__file__).resolve().parent
