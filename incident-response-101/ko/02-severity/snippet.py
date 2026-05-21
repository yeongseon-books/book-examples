"""Generated from book-content article."""

def route_by_severity(sev: str) -> dict:
    policies = {
        "SEV1": {"page": "all", "war_room": True, "cadence": 15},
        "SEV2": {"page": "primary", "war_room": True, "cadence": 30},
        "SEV3": {"page": "primary", "war_room": False, "cadence": 60},
    }
    return policies[sev]
