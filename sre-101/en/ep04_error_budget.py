"""Sre 101 - Episode 4: Error budget."""


def burn_rate(observed_error_ratio: float, allowed_error_ratio: float) -> float:
    """Burn rate."""
    if allowed_error_ratio == 0:
        return 0.0
    return observed_error_ratio / allowed_error_ratio


def mwmb_alert(br_1h: float, br_6h: float) -> bool:
    """Mwmb alert."""
    return br_1h >= 14.4 and br_6h >= 6.0
