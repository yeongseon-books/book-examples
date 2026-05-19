from conftest import load_module

run = load_module("ko/05-multimodal-rag/step01_multimodal_rag.py", "ep05").run


def test_ep05_rag_retrieves_fixture() -> None:
    assert run("receipt") == "doc-1"
