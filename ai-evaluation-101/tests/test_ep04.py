from conftest import load_module


def test_ep04_mock_judge_prefers_grounded_answer() -> None:
    module = load_module("ko/04-llm-as-judge/step01_mock_judge.py", "ep04")
    result = module.run()
    assert result["winner"] == "A"
