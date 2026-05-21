"""Generated from book-content article."""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class DatasetCard:
    name: str
    version: str  # semver: 1.2.0
    source_type: str  # "first-party" | "public" | "scrape" | "vendor"
    source_url: str | None
    license: str  # "CC-BY-4.0" | "MIT" | "proprietary" | etc.
    snapshot_date: str  # ISO 8601
    row_count: int
    size_bytes: int
    sha256: str
    schema: dict
    description: str
    consent_basis: str | None = None  # GDPR/PIPA legal basis
    pii_fields: list = field(default_factory=list)
    retention_days: int | None = None
    owner: str = "unknown"
    tags: list = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)

def fingerprint_file(path: str) -> tuple[str, int]:
    h = hashlib.sha256()
    size = 0
    with open(path, "rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
            size += len(chunk)
    return h.hexdigest(), size
