from conftest import load_module

run = load_module("ko/07-calibration/step01_calibration_demo.py", "ep07").run


def test_ep07_calibration_improves_brier() -> None:
    out = run()
    assert out["platt_brier"] <= out["base_brier"]
    assert out["calibration_bins"] >= 5
