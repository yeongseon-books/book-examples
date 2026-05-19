from pathlib import Path

from ko import _10_build_a_container_app as ep


def test_pipeline_produces_layers_and_valid_manifest(tmp_path: Path):
    app_dir = tmp_path / "tiny_app"
    app_dir.mkdir()
    (app_dir / "main.py").write_text('print("ok")\n', encoding="utf-8")
    result = ep.run_pipeline(app_dir)
    assert int(result["layer_count"]) > 0
    assert int(result["flattened_files"]) > 0
    assert result["manifest_errors"] == []


def test_generated_dockerfile_is_lintable(tmp_path: Path):
    app_dir = tmp_path / "tiny_app"
    app_dir.mkdir()
    dockerfile = ep.generate_dockerfile(app_dir)
    assert "FROM python:3.12-slim" in dockerfile
