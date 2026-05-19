"""Pytest configuration and fixtures for Pytest 101."""

import pytest
from en.ep04_db_like import InMemoryUserDB


@pytest.fixture
def db() -> InMemoryUserDB:
    """Db."""
    return InMemoryUserDB()
