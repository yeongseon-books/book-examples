from pathlib import Path
from typing import Any, cast

from common import read_text
from ko.ep10_portfolio_audit import run_portfolio_audit


def test_ep10_end_to_end_audit(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        read_text(Path("fixtures/sample_readme.md")), encoding="utf-8"
    )
    (tmp_path / "Dockerfile").write_text("FROM python:3.12", encoding="utf-8")
    (tmp_path / ".env.example").write_text("APP_ENV=dev", encoding="utf-8")
    (tmp_path / "requirements.txt").write_text(
        "flask==3.0.3\npytest==8.3.3\n", encoding="utf-8"
    )
    (tmp_path / "app.py").write_text(
        "app.run(host='0.0.0.0', port=8080)", encoding="utf-8"
    )
    (tmp_path / "test_api.py").write_text(
        "def test_api():\n    assert True\n", encoding="utf-8"
    )
    report = cast("dict[str, Any]", run_portfolio_audit(tmp_path))
    assert report["score"] >= 70
    assert report["readme_ok"] is True
