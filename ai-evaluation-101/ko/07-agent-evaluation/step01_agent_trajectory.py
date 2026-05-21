"""Ai Evaluation 101 - 7편: agent evaluation 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run() -> dict[str, float]:
    """Run."""
    expected_tools = ["read_calendar", "read_emails", "summarize", "send_email"]
    actual_tools = ["read_calendar", "read_emails", "summarize", "send_email"]
    success = 1.0 if actual_tools[-1] == "send_email" else 0.0
    matched = sum(
        1 for a, e in zip(actual_tools, expected_tools, strict=False) if a == e
    )
    step_match = matched / len(expected_tools)
    overhead = len(actual_tools) / len(expected_tools)
    return {
        "task_success": success,
        "step_match": step_match,
        "step_overhead": overhead,
    }


if __name__ == "__main__":
    print(run())
