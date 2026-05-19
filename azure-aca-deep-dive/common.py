"""Shared utilities and domain models for Azure Aca Deep Dive."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass


@dataclass
class AzPlan:
    """Az plan."""

    command: str
    payload: dict[str, object]


def dry_run_az(command: str) -> dict[str, object]:
    """Dry run az."""
    completed = subprocess.run(
        ["python3", "-c", f"print({command!r})"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {"stdout": completed.stdout.strip(), "returncode": completed.returncode}


def as_json(data: dict[str, object]) -> str:
    """As json."""
    return json.dumps(data, ensure_ascii=False, indent=2)


def traffic_total(traffic: list[dict[str, int | str]]) -> int:
    """Traffic total."""
    return int(sum(int(item["weight"]) for item in traffic))
