import pytest

from ko import ep09_async


@pytest.mark.asyncio
async def test_ep09_async() -> None:
    assert await ep09_async.run() == 10
