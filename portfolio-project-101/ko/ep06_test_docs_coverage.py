from __future__ import annotations

from pathlib import Path

from common import count_docstrings, list_py_files


def generate_coverage_report(project_root: str | Path) -> dict[str, int]:
    root = Path(project_root)
    py_files = list_py_files(root)
    test_files = [p for p in py_files if "test" in p.name]
    docstrings = sum(count_docstrings(path) for path in py_files)
    return {
        "python_files": len(py_files),
        "test_files": len(test_files),
        "docstring_count": docstrings,
    }
