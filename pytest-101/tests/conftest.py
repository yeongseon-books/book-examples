import pytest
from en.ep04_db_like import InMemoryUserDB


@pytest.fixture
def db() -> InMemoryUserDB:
    return InMemoryUserDB()
