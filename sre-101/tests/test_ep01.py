from common import Incident
from en.ep01_service_health import compute_health


def test_ep01_health_metrics():
    incidents = [Incident(0, 10), Incident(20, 30)]
    out = compute_health(incidents, 100)
    assert out["uptime_ratio"] == 0.8
    assert out["mttr"] == 10
