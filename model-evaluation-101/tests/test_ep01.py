from conftest import load_module

run = load_module("ko/01-why-evaluation-is-hard/step01_leakage_demo.py", "ep01").run


def test_ep01_leakage_inflates_score() -> None:
    out = run()
    assert out["leaked_train_score"] > out["proper_test_score"]
