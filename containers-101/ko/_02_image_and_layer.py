from __future__ import annotations

from common import Layer, flatten_layers


def stack_layers(layers: list[Layer]) -> dict[str, str]:
    return flatten_layers(layers)


def copy_on_write(base: dict[str, str], updates: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    child = dict(base)
    child.update(updates)
    return base, child


def layer_digests(layers: list[Layer]) -> list[str]:
    return [layer.digest() for layer in layers]
