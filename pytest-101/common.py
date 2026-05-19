"""Shared utilities and domain models for Pytest 101."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiResponse:
    """Api response."""

    status_code: int
    payload: dict


def now_iso_utc() -> str:
    """Now iso utc."""
    import datetime as _dt

    return _dt.datetime.now(_dt.timezone.utc).isoformat()
