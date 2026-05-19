from conftest import load_module

run = load_module("ko/01-why-multimodal-matters/step01_why_multimodal.py", "ep01").run


def test_ep01_runs() -> None:
    result = run()
    assert result["shape"] == (8, 8)
