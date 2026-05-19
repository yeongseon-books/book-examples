from common import run_with_exit_code


def test_ep09_runner_exit_code_contract():
    assert run_with_exit_code(lambda: True) == 0
    assert run_with_exit_code(lambda: False) == 1
