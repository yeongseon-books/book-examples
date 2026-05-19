"""Ai Web Dev 101 - Episode 1: Prompt builder."""

from __future__ import annotations


def build_prompt(
    system_role: str,
    task: str,
    constraints: list[str],
    output_format: str,
    examples: list[str] | None = None,
) -> str:
    """Build prompt."""
    lines = [
        f"[SYSTEM]\n{system_role}",
        f"[TASK]\n{task}",
        "[CONSTRAINTS]\n" + "\n".join(f"- {c}" for c in constraints),
        f"[FORMAT]\n{output_format}",
    ]
    if examples:
        lines.append("[EXAMPLES]\n" + "\n".join(examples))
    return "\n\n".join(lines)


def choose_temperature(kind: str) -> float:
    """Choose temperature."""
    return 0.2 if kind in {"code", "extract"} else 0.8
