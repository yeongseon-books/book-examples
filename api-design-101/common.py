from __future__ import annotations

from base64 import urlsafe_b64decode, urlsafe_b64encode
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient


def client_for(app: FastAPI) -> TestClient:
    return TestClient(app)


def now_iso_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def encode_cursor(value: int) -> str:
    return urlsafe_b64encode(str(value).encode("utf-8")).decode("utf-8")


def decode_cursor(token: str | None) -> int:
    if not token:
        return 0
    raw = urlsafe_b64decode(token.encode("utf-8")).decode("utf-8")
    return int(raw)


def problem(status: int, code: str, title: str, detail: str) -> dict[str, Any]:
    return {
        "type": "about:blank",
        "title": title,
        "status": status,
        "code": code,
        "detail": detail,
    }
