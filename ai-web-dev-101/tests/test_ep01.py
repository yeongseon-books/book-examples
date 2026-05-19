from conftest import load_module

first_ai_call = load_module(
    "ko/01-hello-ai-api/step01_first_call.py", "ep01"
).first_ai_call


def test_ep01_tracks_usage_and_answer() -> None:
    result = first_ai_call("한 줄 응원 메시지")
    assert result["is_cost_trackable"] is True
    assert result["total_tokens"] > 0
    assert "정확" in str(result["answer"])
