from conftest import load_module

run = load_module("ko/01-what-is-incident/step01_example.py", "ep01").run

def test_ep01_incident_classification() -> None:
    result = run()
    assert result["classification"] == "incident"
