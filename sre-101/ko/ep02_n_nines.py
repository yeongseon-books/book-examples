"""Sre 101 - Episode 2: N nines."""


def availability_from_nines(nines: float) -> float:
    """Availability from nines."""
    return 1.0 - (10 ** (-nines))


def downtime_budget_minutes(nines: float, period_minutes: int) -> float:
    """Downtime budget minutes."""
    return (1.0 - availability_from_nines(nines)) * period_minutes
