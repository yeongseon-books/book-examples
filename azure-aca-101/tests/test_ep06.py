from conftest import load_module


run = load_module("ko/06-dapr-integration/step01_dapr_sidecar.py", "ep06").run


def test_ep06_dapr_urls_and_scope() -> None:
    data = run()
    assert data["publish"].endswith("/publish/orderpubsub/orders")
    assert data["invoke"].endswith("/invoke/worker-app/method/process")
    assert "api-app" in data["component"]["scopes"]
