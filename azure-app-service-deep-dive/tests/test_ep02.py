from conftest import load_module
from fastapi.testclient import TestClient

create_app = load_module(
    "ko/02-front-end-and-arr/step01_arr_affinity_demo.py", "ep02"
).create_app


def test_ep02_arr_affinity_changes_worker_choice() -> None:
    client = TestClient(create_app())
    sticky = client.get("/route", headers={"Cookie": "ARRAffinity=worker-2"}).json()
    random_pick = client.get("/route").json()
    assert sticky["sticky"] is True
    assert sticky["selected_worker"] == "worker-2"
    assert random_pick["sticky"] is False
    assert random_pick["selected_worker"] == "worker-random"
