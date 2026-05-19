from conftest import load_module

run = load_module("ko/02-train-val-test/step01_split_demo.py", "ep02").run


def test_ep02_stratified_split_and_ratios() -> None:
    out = run()
    assert abs(out["train_ratio"] - 0.6) < 0.01
    assert abs(out["val_ratio"] - 0.2) < 0.01
    assert abs(out["test_ratio"] - 0.2) < 0.01
    assert abs(out["full_pos_rate"] - out["train_pos_rate"]) < 0.02
