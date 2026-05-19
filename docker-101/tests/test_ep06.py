# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/06-env-and-config/step01_env_config_validate.py", "ep06").run


def test_ep06() -> None:
    result = run()
    assert result["success"] is True
    assert result["env"]["LOG_LEVEL"] == "INFO"
