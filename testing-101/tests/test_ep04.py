from ko.ep04_e2e_test import create_app


def test_ep04_e2e_order_success():
    app = create_app()
    client = app.test_client()
    response = client.post("/api/order", json={"item": "book", "qty": 2})
    assert response.status_code == 201
    assert response.get_json()["ok"] is True
