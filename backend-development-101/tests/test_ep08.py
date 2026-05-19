from fastapi.testclient import TestClient

from conftest import load_module


def test_ep08_dependency_override_for_tests() -> None:
    module = load_module("ko/08-testing-the-backend/step01_testable_app.py", "ep08")
    app = module.build_app()
    sink = module.Sink()
    app.dependency_overrides[module.get_sink] = lambda: sink
    client = TestClient(app)
    r = client.post("/messages", json={"text": "hello"})
    assert r.status_code == 200
    assert sink.events == ["message:hello"]
