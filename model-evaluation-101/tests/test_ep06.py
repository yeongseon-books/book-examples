from conftest import load_module

run = load_module("ko/06-roc-and-auc/step01_roc_pr_auc.py", "ep06").run


def test_ep06_auc_reasonable() -> None:
    out = run()
    assert out["auc_roc"] > 0.7
    assert out["auc_pr"] > 0.3
