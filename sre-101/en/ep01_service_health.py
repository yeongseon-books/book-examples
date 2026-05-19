from common import Incident, ratio


def compute_health(incidents: list[Incident], total_minutes: int) -> dict:
    downtime = sum(i.duration for i in incidents)
    uptime = max(0, total_minutes - downtime)
    mttr = ratio(downtime, len(incidents))
    mtbf = ratio(uptime, max(1, len(incidents)))
    return {"uptime_ratio": ratio(uptime, total_minutes), "mttr": mttr, "mtbf": mtbf}
