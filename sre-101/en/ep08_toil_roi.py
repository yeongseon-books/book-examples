from common import ratio


def toil_hours(task_minutes: int, frequency_per_week: int) -> float:
    return (task_minutes * frequency_per_week) / 60.0


def automation_roi(saved_hours_per_week: float, build_hours: float) -> float:
    return ratio(saved_hours_per_week * 52, build_hours)
