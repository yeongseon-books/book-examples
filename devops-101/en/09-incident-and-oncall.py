from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IncidentEvent:
    at: str
    action: str
    details: str


def pick_oncall(engineers: list[str], vacation: set[str], offset: int = 0) -> str:
    available = [engineer for engineer in engineers if engineer not in vacation]
    if not available:
        raise ValueError("No available engineer for on-call")
    return available[offset % len(available)]


def build_postmortem(
    title: str,
    impact: str,
    timeline: list[IncidentEvent],
    root_cause: str,
    actions: list[str],
) -> str:
    lines = [
        f"# Postmortem: {title}",
        "",
        "## Impact",
        impact,
        "",
        "## Timeline",
    ]
    for event in timeline:
        lines.append(f"- {event.at} | {event.action} | {event.details}")
    lines.extend(["", "## Root Cause", root_cause, "", "## Action Items"])
    lines.extend([f"- {item}" for item in actions])
    return "\n".join(lines)
