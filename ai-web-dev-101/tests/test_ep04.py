from conftest import load_module


module = load_module("ko/04-rag-intro/step01_simple_rag.py", "ep04")
search = module.search
answer_with_rag = module.answer_with_rag


def test_ep04_rag_returns_refund_context() -> None:
    context = search("환불 방법 알려줘")
    assert "환불" in context
    answer = answer_with_rag("환불")
    assert "근거:" in answer
