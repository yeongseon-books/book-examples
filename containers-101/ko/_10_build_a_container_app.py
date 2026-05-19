"""Containers 101 - Episode 10: Build a container app."""

from __future__ import annotations

from pathlib import Path

from common import Layer

from ko import _02_image_and_layer as image_layer
from ko import _04_dockerfile as dockerfile_mod
from ko import _07_registry as registry_mod


def generate_dockerfile(app_dir: Path) -> str:
    """Generate dockerfile."""
    return "\n".join(
        [
            "FROM python:3.12-slim",
            "WORKDIR /app",
            "COPY requirements.txt .",
            "RUN pip install --no-cache-dir -r requirements.txt",
            f"COPY {app_dir.name} ./app",
            "USER app",
            'CMD ["python", "app/main.py"]',
        ]
    )


def build_virtual_layers() -> list[Layer]:
    """Build virtual layers."""
    return [
        Layer("base", {"/etc/os-release": "debian"}),
        Layer("deps", {"/site-packages/pytest": "8.3.4"}),
        Layer("app", {"/app/main.py": 'print("ok")'}),
    ]


def run_pipeline(app_dir: Path) -> dict[str, object]:
    """Run pipeline."""
    dockerfile = generate_dockerfile(app_dir)
    lint_warnings = dockerfile_mod.lint_dockerfile(dockerfile)
    layers = build_virtual_layers()
    flattened = image_layer.stack_layers(layers)
    digests = image_layer.layer_digests(layers)
    manifest = {
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "config": {"digest": digests[0]},
        "layers": [{"digest": d} for d in digests],
    }
    return {
        "dockerfile": dockerfile,
        "lint_warnings": lint_warnings,
        "layer_count": len(layers),
        "flattened_files": len(flattened),
        "manifest_errors": registry_mod.validate_manifest(manifest),
    }
