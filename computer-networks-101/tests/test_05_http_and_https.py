"""Tests for 05 http and https in Computer Networks 101."""

from tests._loader import load_ko


def test_parse_and_build() -> None:
    """Test parse and build."""
    ep = load_ko("05-http-and-https")
    raw = "GET /health HTTP/1.1\r\nHost: localhost\r\n\r\n"
    req = ep.parse_http_request(raw)
    assert req["method"] == "GET"
    resp = ep.build_http_response(200, "ok")
    assert b"Content-Length: 2" in resp


def test_local_http_demo() -> None:
    """Test local http demo."""
    ep = load_ko("05-http-and-https")
    out = ep.run_local_http_demo()
    assert out["status"] == 200
    assert out["path"] == "/health"
