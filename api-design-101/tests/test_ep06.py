from __future__ import annotations

from .helpers import client_for, load_module


def test_ep06_cursor_pagination() -> None:
    mod = load_module(
        "ko/06-pagination-and-filtering/step01_pagination_filter.py", "ep06_ko"
    )
    app = mod.build_app()
    c = client_for(app)
    first = c.get("/orders", params={"limit": 5, "status": "paid"}).json()
    second = c.get(
        "/orders", params={"limit": 5, "status": "paid", "cursor": first["next_cursor"]}
    ).json()
    assert len(first["items"]) == 5
    assert first["items"][0]["id"] == 2
    assert second["items"][0]["id"] == 12
