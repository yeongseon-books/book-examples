from fastapi.testclient import TestClient

from conftest import load_module


module = load_module("ko/06-cold-start-and-warmup/step01_warmup_contract.py", "ep06")
create_app = module.create_app
check_ready = module.check_ready


def test_ep06_warmup_contract_and_status_filter() -> None:
    warming = TestClient(create_app(False)).get("/warmup")
    ready = TestClient(create_app(True)).get("/warmup")
    assert warming.status_code == 503
    assert ready.status_code == 200
    assert check_ready(200, {200}) is True
    assert check_ready(503, {200}) is False
