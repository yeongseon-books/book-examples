from conftest import load_module


run = load_module("ko/01-what-is-aca/step01_aca_positioning.py", "ep01").run


def test_ep01_has_up_command_shape() -> None:
    result = run()
    assert result["service"] == "aca"
    assert "az containerapp up" in str(result["command"])
    assert "--ingress external" in str(result["command"])
