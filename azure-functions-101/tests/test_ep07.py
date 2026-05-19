from conftest import run_script


def test_ep07() -> None:
    output = run_script("ko/07-monitoring-and-ops/step01_monitoring_queries.py")
    assert "requests | where timestamp > ago(1h)" in output
