"""Generated from book-content article."""

def build_update(audience: str, sev: str, summary: str, next_min: int) -> dict:
    return {
        "audience": audience,
        "severity": sev,
        "summary": summary,
        "next_update_minutes": next_min,
    }


def cadence_minutes(sev: str) -> int:
    return {"SEV1": 15, "SEV2": 30, "SEV3": 60}.get(sev, 120)
