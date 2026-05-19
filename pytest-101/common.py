from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiResponse:
    status_code: int
    payload: dict


def now_iso_utc() -> str:
    import datetime as _dt

    return _dt.datetime.now(_dt.timezone.utc).isoformat()
