from common import ep02_process_vs_thread


def test_ep02_process_and_thread_ids():
    data = ep02_process_vs_thread()
    assert data["process_pid"] != data["parent_pid"]
    assert data["thread_id"] != 0
