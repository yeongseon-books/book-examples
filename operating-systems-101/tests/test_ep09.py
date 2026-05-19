from common import ep09_syscall_demo


def test_ep09_syscall_io_roundtrip():
    out = ep09_syscall_demo()
    assert out["data"] == "hello"
