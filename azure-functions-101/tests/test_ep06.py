from conftest import run_script


def test_ep06() -> None:
    output = run_script("ko/06-scaling-and-cold-start/step01_scale_simulator.py")
    assert "'instances': 5" in output
