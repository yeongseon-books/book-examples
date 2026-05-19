from ko.ep04_scope_binding import dyn_add, dynamic_scope, lexical_scope


def test_ep04_lexical_and_dynamic_scope():
    assert lexical_scope(2)(3) == 5
    assert dynamic_scope(dyn_add, {"x": 10}, 5) == 15
