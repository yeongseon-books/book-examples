from common import ratio


def compute_sli(successes: int, total: int) -> float:
    return ratio(successes, total)


def is_slo_met(sli: float, slo_target: float) -> bool:
    return sli >= slo_target


def is_sla_breached(sli: float, sla_floor: float) -> bool:
    return sli < sla_floor
