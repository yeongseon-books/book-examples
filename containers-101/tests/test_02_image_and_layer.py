from common import Layer
from ko import _02_image_and_layer as ep


def test_layer_stacking_and_override():
    layers = [
        Layer("base", {"/app/a.txt": "a", "/app/b.txt": "b"}),
        Layer("update", {"/app/b.txt": "B"}),
        Layer("delete", {"/app/a.txt": "__DELETE__"}),
    ]
    fs = ep.stack_layers(layers)
    assert fs["/app/b.txt"] == "B"
    assert "/app/a.txt" not in fs


def test_copy_on_write_keeps_parent_immutable():
    parent = {"/x": "1"}
    original, child = ep.copy_on_write(parent, {"/x": "2"})
    assert original["/x"] == "1"
    assert child["/x"] == "2"
