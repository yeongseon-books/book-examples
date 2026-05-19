"""Tests for ep09 in Web Development 101."""

from en.ep09_performance_caching import app_factory, slow_square


def test_ep09_lru_and_etag_304():
    """Test ep09 lru and etag 304."""
    app = app_factory()
    c = app.test_client()
    first = c.get("/resource")
    etag = first.headers["ETag"]
    second = c.get("/resource", headers={"If-None-Match": etag})
    assert first.status_code == 200
    assert second.status_code == 304
    slow_square.cache_clear()
    _ = slow_square(7)
    _ = slow_square(7)
    assert slow_square.cache_info().hits >= 1
