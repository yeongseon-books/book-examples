"""Sre 101 - Episode 3: Sli slo sla."""

from common import ratio


def compute_sli(successes: int, total: int) -> float:
    """Compute sli."""
    return ratio(successes, total)


def is_slo_met(sli: float, slo_target: float) -> bool:
    """Is slo met."""
    return sli >= slo_target


def is_sla_breached(sli: float, sla_floor: float) -> bool:
    """Is sla breached."""
    return sli < sla_floor
