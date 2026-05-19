from ko.ep04_flask_demo import create_app


def test_ep04_flask_endpoints() -> None:
    app = create_app()
    client = app.test_client()
    r1 = client.get("/health")
    assert r1.status_code == 200
    assert r1.get_json()["status"] == "ok"
    r2 = client.post("/api/echo", json={"x": 1})
    assert r2.status_code == 200
    assert r2.get_json()["echo"]["x"] == 1
