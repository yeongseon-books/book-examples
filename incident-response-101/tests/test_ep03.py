from conftest import load_module

run = load_module("ko/03-initial-response/step01_example.py", "ep03").run


def test_ep03_sev1_routes_to_senior_oncall() -> None:
    result = run()
    assert "senior-ic" in result["responders"]
