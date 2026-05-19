"""Cloud Computing 101 - Episode 1: Region placement."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def choose_region_placement(users: str, disaster_recovery: bool) -> dict[str, object]:
    """Choose region placement."""
    if users == "global" and disaster_recovery:
        regions = ["ap-northeast-2", "us-east-1"]
        az_per_region = 3
    else:
        regions = ["ap-northeast-2"]
        az_per_region = 2
    return record(
        "placement", "select_regions", regions=regions, az_per_region=az_per_region
    )
