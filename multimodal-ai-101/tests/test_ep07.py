"""Tests for ep07 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/07-text-to-image-diffusion/step01_text_to_image.py", "ep07").run


def test_ep07_diffusion_shape() -> None:
    """Test ep07 diffusion shape."""
    assert run("sunset") == (8, 8)
