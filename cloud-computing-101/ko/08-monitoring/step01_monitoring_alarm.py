from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    return {'ok': True, 'service': service, 'action': action, 'payload': payload}


def create_alarm_plan(threshold: float, periods: int) -> dict[str, object]:
    return record('monitoring', 'put_alarm', metric='CPUUtilization', threshold=threshold, evaluation_periods=periods)
