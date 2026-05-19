from conftest import load_module


def test_ep09_welch_detects_variant_a_advantage() -> None:
    module = load_module("ko/09-ab-testing-llms/step01_ab_welch.py", "ep09")
    result = module.run()
    assert result["is_better"] is True
    assert result["p_value"] < 0.05
