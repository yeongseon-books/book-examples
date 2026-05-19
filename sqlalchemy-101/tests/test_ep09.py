"""Tests for ep09 in Sqlalchemy 101."""

import pytest
from ko import ep09_async


@pytest.mark.asyncio
async def test_ep09_async() -> None:
    """Test ep09 async."""
    assert await ep09_async.run() == 10
