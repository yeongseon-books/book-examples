from common import ep07_run_cli


def test_ep07_cli_runs() -> None:
    code, out = ep07_run_cli(["python"])
    assert code == 0
    assert "hello, python" in out
