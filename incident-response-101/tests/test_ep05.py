from conftest import load_module

run = load_module("ko/05-timeline/step01_example.py", "ep05").run

def test_ep05_timeline_events_monotonic() -> None:
    events = run()
    assert events[0]["timestamp"] <= events[1]["timestamp"] <= events[2]["timestamp"]
