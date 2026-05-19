"""Tests for ep02 in Operating Systems 101."""

from common import ep02_process_vs_thread


def test_ep02_process_and_thread_ids():
    """Test ep02 process and thread ids."""
    data = ep02_process_vs_thread()
    assert data["process_pid"] != data["parent_pid"]
    assert data["thread_id"] != 0
