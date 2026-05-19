from conftest import load_module


run = load_module(
    "ko/09-production-operations/step01_observability_cost.py", "ep09"
).run


def test_ep09_observability_fields() -> None:
    result = run("req", "monitor token usage")
    assert "request_id" in result
    assert float(result["cost_usd"]) >= 0.0
