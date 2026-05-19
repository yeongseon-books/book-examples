from conftest import load_module

run = load_module("ko/10-incident-runbook/step01_example.py", "ep10").run


def test_ep10_runbook_fail_fast_stops_after_failure() -> None:
    outcomes = run()
    assert outcomes == [
        {"name": "ack", "result": "passed"},
        {"name": "mitigate", "result": "failed"},
    ]
