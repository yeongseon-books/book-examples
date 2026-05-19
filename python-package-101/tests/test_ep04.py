from pathlib import Path

from common import ep04_run_build_helper


def test_ep04_build_helper_produces_artifacts(tmp_path: Path) -> None:
    out = ep04_run_build_helper(tmp_path)
    assert out["valid"] is True
    assert any(a.endswith(".whl") for a in out["artifacts"])
