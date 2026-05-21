"""Generated from book-content article."""

def relative_alert(current: float, baseline_mean: float, baseline_std: float, k: float = 3.0) -> bool:
    """Alert when current value is more than k std from baseline mean."""
    return abs(current - baseline_mean) > k * baseline_std

# Learn baseline from past 30 days
baseline_mean = 0.03
baseline_std = 0.008
if relative_alert(today_rate, baseline_mean, baseline_std):
    page_oncall("thumbs_down_rate anomaly")
