from __future__ import annotations

import json

from conftest import load_module


def test_observability_payload_and_query() -> None:
    mod = load_module("ko/06-logging-monitoring/step01_observability_basics.py", "ep06")
    payload = json.loads(mod.json_log("checkout_completed", route="/checkout"))
    assert payload["message"] == "checkout_completed"
    assert payload["route"] == "/checkout"
    assert "AppTraces" in mod.kql_error_top_n(15)
    assert mod.correlation_id("abc") == "abc"
