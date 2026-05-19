from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path


def compute_process_metrics(path: str) -> dict[str, float]:
    events = json.loads(Path(path).read_text(encoding="utf-8"))
    lead_times = []
    cycle_times = []
    for e in events:
        started = datetime.fromisoformat(e["started"])
        deployed = datetime.fromisoformat(e["deployed"])
        first_commit = datetime.fromisoformat(e["first_commit"])
        review = datetime.fromisoformat(e["ready_for_review"])
        lead_times.append((deployed - started).total_seconds() / 3600)
        cycle_times.append((review - first_commit).total_seconds() / 3600)
    return {"lead_time_hours": sum(lead_times) / len(lead_times), "cycle_time_hours": sum(cycle_times) / len(cycle_times)}
