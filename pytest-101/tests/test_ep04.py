import pytest

from en.ep04_db_like import InMemoryUserDB


@pytest.fixture(scope="function")
def local_db() -> InMemoryUserDB:
    db = InMemoryUserDB()
    db.add_user(1, "alice")
    return db


def test_ep04_function_fixture(local_db):
    assert local_db.get_user(1) == "alice"


def test_ep04_module_fixture(module_tag):
    assert module_tag == "pytest-101"
