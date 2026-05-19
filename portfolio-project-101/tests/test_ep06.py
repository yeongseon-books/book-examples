from pathlib import Path

from ko.ep06_test_docs_coverage import generate_coverage_report


def test_ep06_coverage_report(tmp_path: Path) -> None:
    (tmp_path / "m.py").write_text(
        '"""module"""\n\n\ndef a():\n    """d"""\n    return 1\n', encoding="utf-8"
    )
    (tmp_path / "test_m.py").write_text(
        "def test_x():\n    assert True\n", encoding="utf-8"
    )
    report = generate_coverage_report(tmp_path)
    assert report["python_files"] == 2
    assert report["test_files"] == 1
    assert report["docstring_count"] >= 2
