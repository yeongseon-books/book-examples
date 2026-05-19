"""Tests for 06 isolation levels in Database Systems 101."""

from conftest import load_ko_module


def test_dirty_read_vs_serializable_visibility():
    """Test dirty read vs serializable visibility."""
    m = load_ko_module("06-isolation-levels.py")
    s = m.VersionedKVStore()
    t1 = s.begin()
    s.write(t1, "x", 10)
    t2 = s.begin()
    assert s.read(t2, "x", "read_uncommitted") == 10
    assert s.read(t2, "x", "serializable", snapshot_tx=t2) is None


def test_phantom_read_behavior():
    """Test phantom read behavior."""
    m = load_ko_module("06-isolation-levels.py")
    assert m.phantom_read_demo("read_committed") == (1, 2)
    assert m.phantom_read_demo("serializable") == (1, 1)
