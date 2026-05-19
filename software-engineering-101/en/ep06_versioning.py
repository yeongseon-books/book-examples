from __future__ import annotations

from common import BranchMachine, semver_bump


def changelog_parser(text: str) -> dict[str, int]:
    return {
        "feat": sum(1 for l in text.splitlines() if l.strip().startswith("- feat:")),
        "fix": sum(1 for l in text.splitlines() if l.strip().startswith("- fix:")),
    }


def branch_state_machine(events: list[str]) -> str:
    machine = BranchMachine()
    for event in events:
        machine.apply(event)
    return machine.state


__all__ = ["semver_bump", "changelog_parser", "branch_state_machine"]
