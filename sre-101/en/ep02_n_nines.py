def availability_from_nines(nines: float) -> float:
    return 1.0 - (10 ** (-nines))


def downtime_budget_minutes(nines: float, period_minutes: int) -> float:
    return (1.0 - availability_from_nines(nines)) * period_minutes
