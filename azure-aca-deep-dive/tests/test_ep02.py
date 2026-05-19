from conftest import load_module

run = load_module(
    "ko/02-environment-internals/step01_environment_boundary.py", "ep02"
).run


def test_ep02_environment_boundary_flags() -> None:
    result = run()
    assert result["episode"] == 2
    assert result["plan"]["shared_network_boundary"] is True
    assert result["plan"]["shared_log_analytics"] is True
