from ko.ep06_objects_prototypes import create_object, get


def test_ep06_prototype_chain_lookup():
    proto = create_object(None, kind="animal")
    dog = create_object(proto, sound="woof")
    assert get(dog, "kind") == "animal"
