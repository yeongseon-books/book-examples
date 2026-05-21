"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class IncidentSignal:
    users: int
    minutes: int
    core_path_impacted: bool
    error_ratio: float


def decide(signal: IncidentSignal) -> str:
    if signal.core_path_impacted and signal.error_ratio >= 0.05:
        return "incident"
    if signal.users >= 1000 or signal.minutes >= 15:
        return "incident"
    return "bug"
