"""Tests for ep06 in Programming Languages 101."""

from ko.ep06_objects_prototypes import create_object, get


def test_ep06_prototype_chain_lookup():
    """Test ep06 prototype chain lookup."""
    proto = create_object(None, kind="animal")
    dog = create_object(proto, sound="woof")
    assert get(dog, "kind") == "animal"
