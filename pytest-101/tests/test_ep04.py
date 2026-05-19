"""Tests for ep04 in Pytest 101."""

import pytest
from en.ep04_db_like import InMemoryUserDB


@pytest.fixture(scope="function")
def local_db() -> InMemoryUserDB:
    """Local db."""
    db = InMemoryUserDB()
    db.add_user(1, "alice")
    return db


def test_ep04_function_fixture(local_db):
    """Test ep04 function fixture."""
    assert local_db.get_user(1) == "alice"


def test_ep04_module_fixture(module_tag):
    """Test ep04 module fixture."""
    assert module_tag == "pytest-101"
