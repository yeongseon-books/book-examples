from conftest import load_module


def test_ep07_monitoring_queries_and_alert_targets() -> None:
    ko = load_module("ko/07-monitoring-and-ops/step01_monitoring_queries.py", "ep07_ko")
    en = load_module("en/07-monitoring-and-ops/step01_monitoring_queries.py", "ep07_en")
    for module in (ko, en):
        queries = module.build_kql_queries()
        targets = module.build_alert_targets()
        assert "KubeEvents" in queries["recent_events"]
        assert "ContainerLogV2" in queries["pod_logs"]
        assert "node_not_ready" in targets
