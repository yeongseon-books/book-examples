from conftest import load_module

mod = load_module("ko/01-what-is-a-compiler.py", "ep01")


def test_pipeline_output() -> None:
    result = mod.compile_pipeline("2 + 3 * 4")
    assert result["output"] == 14
    assert result["ir"][-1] == "ret t2"
