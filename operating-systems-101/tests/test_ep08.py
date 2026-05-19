from common import ep08_in_memory_fs
from typing import Any, cast


def test_ep08_in_memory_and_tempfile_demo():
    out = cast(dict[str, Any], ep08_in_memory_fs())
    assert "docs" in out["listing"]
    assert out["note"] == "os101"
    assert out["real_content"] == "real"
