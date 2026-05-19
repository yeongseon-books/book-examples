from conftest import load_module


def test_ep05_rubric_gate_passes_high_quality_answer() -> None:
    module = load_module("ko/05-rubric-based-scoring/step01_rubric_scoring.py", "ep05")
    result = module.run()
    assert result["scores"]["correctness"] >= 4
    assert result["verdict"] == "PASS"
