from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass


@dataclass
class AzPlan:
    command: str
    payload: dict[str, object]


def dry_run_az(command: str) -> dict[str, object]:
    completed = subprocess.run(
        ["python3", "-c", f"print({command!r})"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {"stdout": completed.stdout.strip(), "returncode": completed.returncode}


def as_json(data: dict[str, object]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def traffic_total(traffic: list[dict[str, int | str]]) -> int:
    return int(sum(int(item["weight"]) for item in traffic))
