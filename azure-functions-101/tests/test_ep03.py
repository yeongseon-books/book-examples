from conftest import run_script


def test_ep03() -> None:
    output = run_script("ko/03-host-and-worker/step01_host_worker_flow.py")
    assert "worker: handled http.hello" in output
