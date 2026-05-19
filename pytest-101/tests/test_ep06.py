"""Tests for ep06 in Pytest 101."""

from unittest.mock import Mock

import pytest
from common import ApiResponse
from en.ep06_external import fetch_exchange_rate


def test_ep06_external_call_with_unittest_mock():
    """Test ep06 external call with unittest mock."""
    http_get = Mock(return_value=ApiResponse(status_code=200, payload={"rate": 1325.4}))
    rate = fetch_exchange_rate(http_get, base="KRW")
    assert rate == 1325.4
    http_get.assert_called_once()


def test_ep06_external_call_with_monkeypatch(monkeypatch):
    """Test ep06 external call with monkeypatch."""

    class Client:
        """Client."""

        def get(self, _url):
            """Get."""
            return ApiResponse(status_code=500, payload={})

    client = Client()
    monkeypatch.setattr(
        client, "get", lambda _url: ApiResponse(status_code=200, payload={"rate": 1.2})
    )
    assert fetch_exchange_rate(client.get) == 1.2


def test_ep06_external_error_case():
    """Test ep06 external error case."""
    with pytest.raises(RuntimeError):
        fetch_exchange_rate(lambda _url: ApiResponse(status_code=503, payload={}))
