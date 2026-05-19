from en.ep05_frontend_backend import run


def test_ep05_api_contract():
    app = run()
    c = app.test_client()
    r = c.get("/api/data")
    data = r.get_json()
    assert r.status_code == 200
    assert set(data.keys()) == {"message", "version"}
