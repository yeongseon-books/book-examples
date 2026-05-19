"""Containers 101 - Episode 7: Registry."""

from __future__ import annotations

import re

DIGEST_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")
VALID_MEDIA_TYPES = {
    "application/vnd.docker.distribution.manifest.v2+json",
    "application/vnd.oci.image.manifest.v1+json",
}


def validate_manifest(manifest: dict) -> list[str]:
    """Validate manifest."""
    errors: list[str] = []
    if manifest.get("mediaType") not in VALID_MEDIA_TYPES:
        errors.append("unsupported mediaType")

    cfg = manifest.get("config")
    if not isinstance(cfg, dict) or not DIGEST_PATTERN.match(cfg.get("digest", "")):
        errors.append("config digest format is invalid")

    layers = manifest.get("layers")
    if not isinstance(layers, list) or not layers:
        errors.append("layers must be non-empty")
    else:
        for idx, layer in enumerate(layers):
            if not DIGEST_PATTERN.match(layer.get("digest", "")):
                errors.append(f"layer {idx} digest format is invalid")
    return errors
