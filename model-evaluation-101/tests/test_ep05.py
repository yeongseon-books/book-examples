from conftest import load_module


run = load_module("ko/05-f1-score/step01_fbeta_demo.py", "ep05").run


def test_ep05_f1_harmonic_properties() -> None:
    out = run()
    assert out["f1"] <= max(out["precision"], out["recall"])
    assert out["f1"] >= min(out["precision"], out["recall"])
