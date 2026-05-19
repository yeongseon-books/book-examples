from en.ep04_http_api import run


def test_ep04_rest_crud_verbs():
    app = run()
    c = app.test_client()
    assert c.get("/api/v1/items").status_code == 200
    created = c.post("/api/v1/items", json={"name": "pen"})
    assert created.status_code == 201
    item_id = created.get_json()["id"]
    updated = c.put(f"/api/v1/items/{item_id}", json={"name": "pencil"})
    assert updated.status_code == 200
    deleted = c.delete(f"/api/v1/items/{item_id}")
    assert deleted.status_code == 204
