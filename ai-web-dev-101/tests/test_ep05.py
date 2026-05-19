from conftest import load_module

run_agent = load_module("ko/05-ai-agent/step01_tool_agent.py", "ep05").run_agent


def test_ep05_agent_runs_tools_and_returns_amount() -> None:
    result = run_agent("100달러를 환율 계산하고 수수료 적용해줘")
    assert result["steps"] >= 2
    assert "원" in str(result["result"])
