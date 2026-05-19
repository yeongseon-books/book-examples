from ko.ep05_rag_chain import run_chain


def test_ep05_chain_returns_prompt_and_answer():
    out = run_chain("What is overlap?", fixtures_dir="fixtures")
    assert "Context:" in out["prompt"]
    assert "[MOCK_ANSWER]" in out["answer"]
