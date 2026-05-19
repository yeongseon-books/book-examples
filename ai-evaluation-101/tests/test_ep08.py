from conftest import load_module


def test_ep08_regression_gate_passes_thresholds() -> None:
    module = load_module("ko/08-regression-testing/step01_regression_gate.py", "ep08")
    result = module.run()
    assert result["passed"] is True
    assert result["failed"] == []
