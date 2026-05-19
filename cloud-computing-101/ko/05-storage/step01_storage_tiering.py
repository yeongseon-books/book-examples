from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    return {'ok': True, 'service': service, 'action': action, 'payload': payload}


def storage_lifecycle_plan(hot_days: int) -> dict[str, object]:
    transitions = [{'days': hot_days, 'class': 'STANDARD_IA'}, {'days': hot_days + 90, 'class': 'GLACIER'}]
    return record('storage', 'set_lifecycle', transitions=transitions)
