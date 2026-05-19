"""Shared utilities and domain models for Capstone Project 101."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


def best_by_total(score_table: dict[str, list[int]]) -> tuple[str, dict[str, int]]:
    """Best by total."""
    totals = {k: sum(v) for k, v in score_table.items()}
    pick = max(totals.items(), key=lambda item: item[1])[0]
    return pick, totals


def score_stack(
    familiarity: dict[str, int], learning_cost: dict[str, int], ops_cost: dict[str, int]
) -> dict[str, int]:
    """Score stack."""
    keys = familiarity.keys()
    return {k: familiarity[k] - learning_cost[k] - ops_cost[k] for k in keys}


def kpt_actionability(kpt: dict[str, list[str]], actions: list[dict[str, str]]) -> bool:
    """Kpt actionability."""
    return bool(kpt.get("problem")) and all(
        {"who", "what", "by"} <= set(a.keys()) for a in actions
    )


@dataclass(frozen=True)
class MilestonePlan:
    """Milestone plan."""

    milestones: list[str]
    weeks: dict[int, str]
    buffer_days: float

    def has_buffer(self) -> bool:
        """Has buffer."""
        return self.buffer_days > 0


class OfflineOnlyError(RuntimeError):
    """Offline only error."""

    pass


def assert_offline(config: Mapping[str, object]) -> None:
    """Assert offline."""
    if config.get("use_network", False):
        raise OfflineOnlyError("Network access is not allowed in this repository.")
