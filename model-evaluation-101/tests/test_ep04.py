from conftest import load_module

run = load_module("ko/04-precision-and-recall/step01_threshold_tradeoff.py", "ep04").run


def test_ep04_threshold_tradeoff() -> None:
    out = run()
    assert out["t07"]["precision"] >= out["t03"]["precision"]
    assert out["t03"]["recall"] >= out["t07"]["recall"]
