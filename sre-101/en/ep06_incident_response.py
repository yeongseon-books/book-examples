TRANSITIONS = {
    "Detected": ["Triaged"],
    "Triaged": ["Mitigated"],
    "Mitigated": ["Resolved"],
    "Resolved": [],
}


def next_state(current: str, target: str) -> str:
    if target not in TRANSITIONS.get(current, []):
        raise ValueError("invalid transition")
    return target


def should_page(severity: str, minutes_open: int) -> bool:
    if severity == "SEV1":
        return True
    return bool(severity == "SEV2" and minutes_open >= 15)
