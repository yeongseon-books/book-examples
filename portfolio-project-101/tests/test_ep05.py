from pathlib import Path

from ko.ep05_deployment_readiness import check_deployment_readiness


def test_ep05_deployment_readiness(tmp_path: Path) -> None:
    (tmp_path / "Dockerfile").write_text("FROM python:3.12", encoding="utf-8")
    (tmp_path / ".env.example").write_text("APP_ENV=dev", encoding="utf-8")
    (tmp_path / "requirements.txt").write_text(
        "flask==3.0.3\npytest==8.3.3\n", encoding="utf-8"
    )
    (tmp_path / "app.py").write_text(
        "app.run(host='0.0.0.0', port=8080)", encoding="utf-8"
    )
    result = check_deployment_readiness(tmp_path)
    assert all(result.values())
