from conftest import load_module


run = load_module("ko/10-evaluation-report/step01_evaluation_report.py", "ep10").run


def test_ep10_report_has_expected_keys() -> None:
    out = run()
    keys = {
        "threshold",
        "n_samples",
        "positive_rate",
        "accuracy",
        "precision",
        "recall",
        "f1",
        "auc_roc",
        "brier",
        "confusion_matrix",
    }
    assert keys.issubset(out.keys())
