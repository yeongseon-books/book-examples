from conftest import load_module

run = load_module("ko/03-vlm-architecture/step01_vlm_architecture.py", "ep03").run


def test_ep03_vlm_returns_string() -> None:
    assert isinstance(run("table"), str)
