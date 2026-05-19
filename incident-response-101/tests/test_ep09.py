from conftest import load_module

run = load_module("ko/09-prevention/step01_example.py", "ep09").run

def test_ep09_prevention_registry_status_tracking() -> None:
    items = run()
    assert items[0]["status"] == "done"
    assert items[1]["status"] == "open"
