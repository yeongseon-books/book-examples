"""Generated from book-content article."""


def runbook_health(has_sev_map: bool, has_oncall: bool, has_comms: bool, has_drill: bool) -> str:
    score = sum([has_sev_map, has_oncall, has_comms, has_drill])
    if score == 4:
        return "healthy"
    if score >= 2:
        return "needs_improvement"
    return "critical"
