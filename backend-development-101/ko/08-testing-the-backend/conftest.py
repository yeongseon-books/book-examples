# tests/conftest.py
import pytest
from db import Base
from sqlalchemy import create_engine


@pytest.fixture
def engine():
    e = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(e)
    return e
