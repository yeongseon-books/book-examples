"""Software Engineering 101 - Episode 4: Review."""

from __future__ import annotations

import re


def diff_stat_analyzer(diff_text: str) -> dict[str, dict[str, int]]:
    """Diff stat analyzer."""
    result: dict[str, dict[str, int]] = {}
    current = None
    for line in diff_text.splitlines():
        if line.startswith("diff --git"):
            m = re.search(r" b/(\S+)", line)
            if m:
                current = m.group(1)
                result[current] = {"additions": 0, "deletions": 0}
        elif current and line.startswith("+") and not line.startswith("+++"):
            result[current]["additions"] += 1
        elif current and line.startswith("-") and not line.startswith("---"):
            result[current]["deletions"] += 1
    return result


def review_checklist_score(items: dict[str, bool]) -> float:
    """Review checklist score."""
    if not items:
        return 0.0
    return round((sum(items.values()) / len(items)) * 100, 1)
