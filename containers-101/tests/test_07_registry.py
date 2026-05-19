"""Tests for 07 registry in Containers 101."""

from ko import _07_registry as ep


def test_manifest_validation_accepts_valid_payload():
    """Test manifest validation accepts valid payload."""
    digest = "sha256:" + "a" * 64
    manifest = {
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "config": {"digest": digest},
        "layers": [{"digest": digest}],
    }
    assert ep.validate_manifest(manifest) == []


def test_invalid_digest_rejected():
    """Test invalid digest rejected."""
    manifest = {
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "config": {"digest": "sha256:xyz"},
        "layers": [{"digest": "sha256:xyz"}],
    }
    errors = ep.validate_manifest(manifest)
    assert any("digest format is invalid" in e for e in errors)
