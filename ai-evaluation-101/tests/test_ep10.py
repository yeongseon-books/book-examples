from conftest import load_module


def test_ep10_alert_triggers_on_large_shift() -> None:
    module = load_module(
        "ko/10-production-evaluation/step01_continuous_eval.py", "ep10"
    )
    result = module.run()
    assert result["drift_alert"] is True
    assert result["z_gap"] >= 3.0
