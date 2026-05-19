import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_module(rel_path: str):
    path = ROOT / rel_path
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep01_counter_increments():
    from common import ObservabilityStack

    stack = ObservabilityStack()
    stack.handle_request("/x", 0.1, 200)
    stack.handle_request("/x", 0.2, 200)
    out = stack.registry.export_openmetrics()
    assert 'http_requests_total{path="/x",status="200"} 2.0' in out


def test_ep02_metric_log_trace_exist():
    mod = load_module("ko/02-metric-log-trace.py")
    text, log_count, span_count = mod.run_demo()
    assert "requests_total" in text
    assert log_count == 1
    assert span_count == 1


def test_ep03_histogram_buckets_present():
    mod = load_module("ko/03-metric-collection.py")
    out = mod.run_demo()
    assert "http_duration_seconds_bucket" in out
    assert "http_duration_seconds_count" in out


def test_ep04_logger_json_with_context():
    mod = load_module("ko/04-structured-logging.py")
    line = mod.run_demo()
    data = json.loads(line)
    assert data["event"] == "login_failed"
    assert data["service"] == "auth"


def test_ep05_trace_parent_child_relationship():
    from common import Tracer

    tracer = Tracer()
    with tracer.start_span("root"), tracer.start_span("child"):
        pass
    spans = {s.name: s for s in tracer.spans}
    assert spans["child"].parent_id == spans["root"].span_id


def test_ep06_dashboard_sparkline_and_summary():
    mod = load_module("ko/06-dashboard-design.py")
    spark, summary = mod.run_demo()
    assert len(spark) == 5
    assert summary["max"] == 0.9


def test_ep07_alert_fires_with_duration_and_routes():
    mod = load_module("ko/07-alert-and-oncall.py")
    fired, owner = mod.run_demo()
    assert any(a["rule"] == "high_error" for a in fired)
    assert owner == "primary-rotation"


def test_ep08_slo_burn_rate_computation():
    mod = load_module("ko/08-sli-and-slo.py")
    sli, budget, burn = mod.run_demo()
    assert sli == 0.998
    assert budget == 0.0
    assert burn > 1.0


def test_ep09_cardinality_explosion_threshold():
    mod = load_module("ko/09-cost-and-cardinality.py")
    result = mod.run_demo()
    assert result["unique_series"] > 1000
    assert result["explosion"] is True


def test_ep10_stack_composes_signals():
    mod = load_module("ko/10-production-observability-stack.py")
    metrics, logs, spans = mod.run_demo()
    assert "http_requests_total" in metrics
    assert logs == 2
    assert spans == 2
