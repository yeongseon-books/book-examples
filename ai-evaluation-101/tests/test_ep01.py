from conftest import load_module


def test_ep01_accuracy_shows_non_deterministic_risk() -> None:
    module = load_module("ko/01-why-evaluate-llm-apps/step01_eval_basics.py", "ep01")
    result = module.run()
    assert result["accuracy"] < 1.0
