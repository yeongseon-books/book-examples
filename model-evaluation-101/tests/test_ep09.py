from conftest import load_module

run = load_module("ko/09-error-analysis/step01_error_analysis.py", "ep09").run


def test_ep09_error_analysis_outputs() -> None:
    out = run()
    assert "TP=" in out["confusion"]
    assert isinstance(out["misclassified_examples"], list)
    assert len(out["misclassified_examples"]) <= 5
