from pathlib import Path

from common import ep10_generate_template


def test_ep10_generate_skeleton(tmp_path: Path) -> None:
    out = ep10_generate_template(tmp_path, project_name="pkg10")
    root = Path(out["root"])
    assert (root / "pyproject.toml").exists()
    assert (root / "src" / "pkg10" / "__init__.py").exists()
