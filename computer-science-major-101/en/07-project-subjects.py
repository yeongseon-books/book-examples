from pathlib import Path


def generate_project_skeleton(base_dir: Path, project_name: str) -> Path:
    root = base_dir / project_name
    _ = (root / "src").mkdir(parents=True, exist_ok=True)
    _ = (root / "tests").mkdir(parents=True, exist_ok=True)
    _ = (root / "README.md").write_text(
        f"# {project_name}\n\nproject scaffold\n", encoding="utf-8"
    )
    _ = (root / "requirements.txt").write_text("pytest==8.3.4\n", encoding="utf-8")
    _ = (root / "src" / "main.py").write_text(
        "def main():\n    return 'ok'\n", encoding="utf-8"
    )
    _ = (root / "tests" / "test_smoke.py").write_text(
        "from src.main import main\n\ndef test_main():\n    assert main() == 'ok'\n",
        encoding="utf-8",
    )
    return root


if __name__ == "__main__":
    out = generate_project_skeleton(Path("."), "demo-project")
    print(out)
