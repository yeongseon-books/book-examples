from common import ep10_mmap_demo, ep10_namespace_simulator
from typing import Any, cast


def test_ep10_namespace_isolation_model_and_mmap():
    out = cast(dict[str, Any], ep10_namespace_simulator())
    assert out["host"]["pid_ns"] != out["container"]["pid_ns"]
    assert "/app" in out["container"]["mnt_ns"]
    assert ep10_mmap_demo() == ord("a")
