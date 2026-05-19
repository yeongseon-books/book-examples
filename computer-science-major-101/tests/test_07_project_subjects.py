from pathlib import Path

from conftest import load_module


def test_project_skeleton_generator_creates_expected_layout(tmp_path: Path) -> None:
    mod = load_module("ko/07-project-subjects.py")
    root = mod.generate_project_skeleton(tmp_path, "course-tool")
    expected = [
        root / "src",
        root / "tests",
        root / "README.md",
        root / "requirements.txt",
        root / "src" / "main.py",
        root / "tests" / "test_smoke.py",
    ]
    for path in expected:
        assert path.exists()
