"""Shared utilities and domain models for Incident Response 101."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Final, cast


def now_iso() -> str:
    """Now iso."""
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Incident:
    """Incident."""

    id: str
    title: str
    severity: str
    status: str = "open"
    opened_at: str = field(default_factory=now_iso)
    closed_at: str | None = None
    events: list[dict[str, str]] = field(default_factory=list)

    def close(self) -> None:
        """Close."""
        self.status = "closed"
        self.closed_at = now_iso()


class SeverityClassifier:
    """Severity classifier."""

    def classify(self, users_affected: int, revenue_loss: int, regions: int) -> str:
        """Classify."""
        if users_affected >= 100000 or revenue_loss >= 100000 or regions >= 3:
            return "SEV1"
        if users_affected >= 10000 or revenue_loss >= 10000 or regions >= 2:
            return "SEV2"
        if users_affected >= 1000 or revenue_loss >= 1000:
            return "SEV3"
        return "SEV4"


class OnCallRouter:
    """On call router."""

    POLICY: dict[str, dict[str, list[str]]] = {
        "payments": {
            "SEV1": ["senior-ic", "payments-primary", "comms-lead"],
            "SEV2": ["payments-primary", "payments-secondary"],
            "SEV3": ["payments-primary"],
            "SEV4": ["payments-primary"],
        },
        "search": {
            "SEV1": ["senior-ic", "search-primary", "comms-lead"],
            "SEV2": ["search-primary", "search-secondary"],
            "SEV3": ["search-primary"],
            "SEV4": ["search-primary"],
        },
    }

    def route(self, severity: str, service: str) -> list[str]:
        """Route."""
        svc = self.POLICY.get(service, {})
        if severity in svc:
            return svc[severity]
        return ["global-primary"]


class IncidentTimeline:
    """Incident timeline."""

    def __init__(self) -> None:
        self.events: list[dict[str, str]] = []

    def append(
        self, actor: str, action: str, timestamp: str | None = None
    ) -> dict[str, str]:
        """Append."""
        ts = timestamp or now_iso()
        if self.events and ts < self.events[-1]["timestamp"]:
            raise ValueError("timeline must be monotonic")
        event = {"timestamp": ts, "actor": actor, "action": action}
        self.events.append(event)
        return event


class CommsTemplateRenderer:
    """Comms template renderer."""

    def render(self, audience: str, incident: Incident, summary: str) -> str:
        """Render."""
        base = f"[{incident.severity}] {incident.id} {incident.title}: {summary}"
        if audience == "customer":
            return f"Customer Update: {base}"
        if audience == "internal":
            return f"Internal Update: {base}"
        if audience == "stakeholder":
            return f"Stakeholder Update: {base}"
        return f"General Update: {base}"


class RCAFramework:
    """RCA framework."""

    def five_whys(self, problem: str, answers: list[str]) -> dict[str, object]:
        """Five whys."""
        chain = [problem] + answers[:5]
        return {"method": "5-whys", "chain": chain, "root_cause": chain[-1]}

    def fishbone(self, categories: dict[str, list[str]]) -> dict[str, object]:
        """Fishbone."""
        total = sum(len(v) for v in categories.values())
        return {"method": "fishbone", "categories": categories, "factor_count": total}


class MitigationTracker:
    """Mitigation tracker."""

    TRANSITIONS: Final[dict[str, str]] = {
        "proposed": "applied",
        "applied": "verified",
        "verified": "verified",
    }

    def __init__(self) -> None:
        self.state: str = "proposed"

    def advance(self) -> str:
        """Advance."""
        self.state = self.TRANSITIONS[self.state]
        return self.state


class PostmortemGenerator:
    """Postmortem generator."""

    SECTIONS: Final[tuple[str, ...]] = (
        "Summary",
        "Impact",
        "Timeline",
        "Root Cause",
        "Mitigation and Resolution",
        "Action Items",
    )

    def generate(self, incident: Incident, actions: list[dict[str, str]]) -> str:
        """Generate."""
        lines = [f"# Postmortem: {incident.id} - {incident.title}", ""]
        for section in self.SECTIONS:
            lines.append(f"## {section}")
            if section == "Summary":
                lines.append(f"- Severity: {incident.severity}")
                lines.append(f"- Status: {incident.status}")
            elif section == "Timeline":
                for e in incident.events:
                    lines.append(f"- {e['timestamp']} | {e['actor']} | {e['action']}")
            elif section == "Action Items":
                for a in actions:
                    lines.append(
                        f"- [{a['status']}] {a['title']} ({a['owner']}, due {a['due_date']})"
                    )
            else:
                lines.append("- TBD")
            lines.append("")
        return "\n".join(lines).strip() + "\n"


class PreventionTracker:
    """Prevention tracker."""

    def __init__(self) -> None:
        self.items: list[dict[str, str]] = []

    def add(self, title: str, owner: str, due_date: str) -> dict[str, str]:
        """Add."""
        item = {
            "id": f"ACT-{len(self.items) + 1:03d}",
            "title": title,
            "owner": owner,
            "due_date": due_date,
            "status": "open",
        }
        self.items.append(item)
        return item

    def set_status(self, item_id: str, status: str) -> None:
        """Set status."""
        for item in self.items:
            if item["id"] == item_id:
                item["status"] = status
                return
        raise KeyError(item_id)


class RunbookExecutor:
    """Runbook executor."""

    def load(self, text: str) -> dict[str, object]:
        """Load."""
        parsed_raw = json.loads(text)  # pyright: ignore[reportAny]
        if not isinstance(parsed_raw, dict):
            raise ValueError("runbook must be an object")
        parsed = cast("dict[str, object]", parsed_raw)
        if "steps" not in parsed:
            raise ValueError("runbook missing steps")
        return parsed

    def execute(
        self, runbook: dict[str, object], context: dict[str, object]
    ) -> list[dict[str, object]]:
        """Execute."""
        outcomes: list[dict[str, object]] = []
        fail_fast = bool(runbook.get("fail_fast", True))
        steps = runbook.get("steps")
        if not isinstance(steps, list):
            raise ValueError("steps must be a list")
        for step_raw in steps:  # pyright: ignore[reportUnknownVariableType]
            if not isinstance(step_raw, dict):
                raise ValueError("step must be an object")
            step = cast("dict[str, object]", step_raw)
            condition = step.get("when")
            if isinstance(condition, str) and context.get(condition) is not True:
                outcomes.append(
                    {"name": str(step.get("name", "unknown")), "result": "skipped"}
                )
                continue
            success = bool(step.get("success", True))
            result = "passed" if success else "failed"
            outcomes.append(
                {"name": str(step.get("name", "unknown")), "result": result}
            )
            if not success and fail_fast:
                break
        return outcomes
