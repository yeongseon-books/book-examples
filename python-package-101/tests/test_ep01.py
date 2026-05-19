from pathlib import Path

from common import ep01_detect_package_vs_module


def test_ep01_detect_package_and_module(tmp_path: Path) -> None:
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "mod.py").write_text("x = 1\n", encoding="utf-8")
    assert ep01_detect_package_vs_module("pkg", tmp_path)["kind"] == "package"
    assert ep01_detect_package_vs_module("mod", tmp_path)["kind"] == "module"
