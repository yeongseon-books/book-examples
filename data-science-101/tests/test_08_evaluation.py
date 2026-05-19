from _loader import load_module

m = load_module("08-evaluation.py")


def test_episode_08_manual_metrics_match_sklearn() -> None:
    result = m.compare_metrics(seed=42)
    assert abs(result["manual_f1"] - result["sklearn_f1"]) < 1e-9
    assert abs(result["manual_rmse"] - result["sklearn_rmse"]) < 1e-9
