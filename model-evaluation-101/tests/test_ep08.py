from conftest import load_module

run = load_module("ko/08-cross-validation/step01_cross_validation_demo.py", "ep08").run


def test_ep08_kfold_returns_n_scores() -> None:
    out = run()
    assert out["n_scores"] == 5
    assert out["std"] >= 0.0
