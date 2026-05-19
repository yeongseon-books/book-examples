from conftest import run_script


def test_ep05() -> None:
    output = run_script("ko/05-choosing-a-plan/step01_plan_selector.py")
    assert "Flex Consumption" in output
