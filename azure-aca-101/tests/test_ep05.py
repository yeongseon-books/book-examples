from conftest import load_module

run = load_module("ko/05-scaling-with-keda/step01_keda_scaling.py", "ep05").run


def test_ep05_keda_scaling_behaviour() -> None:
    data = run()
    assert data["http_replicas"] == 3
    assert data["worker_replicas"] == 6
