from conftest import load_module

run = load_module("ko/06-root-cause-analysis/step01_example.py", "ep06").run


def test_ep06_five_whys_has_six_nodes() -> None:
    result = run()
    assert len(result["five_whys"]["chain"]) == 6
