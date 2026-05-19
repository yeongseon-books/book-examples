from __future__ import annotations

from conftest import load_module

common = load_module("common.py", "common_mod")


def test_ep01_pipeline_result() -> None:
    ep = load_module("ko/01-what-is-fp.py", "ep01")
    assert ep.price_pipeline(5000) == 8730


def test_ep02_pure_function_deterministic() -> None:
    ep = load_module("ko/02-pure-functions.py", "ep02")
    assert ep.apply_discount(10000, 0.1) == ep.apply_discount(10000, 0.1)


def test_ep03_immutability() -> None:
    ep = load_module("ko/03-immutable-data.py", "ep03")
    state = common.ImmutableState(values=(1, 2))
    nxt = ep.next_state(state, 3)
    assert state.values == (1, 2)
    assert nxt.values == (1, 2, 3)
    assert ep.impossible_mutation(state) is not None


def test_ep04_higher_order_behavior() -> None:
    ep = load_module("ko/04-higher-order-functions.py", "ep04")
    assert ep.apply_to_items([1, 2, 3], lambda x: x + 5) == [6, 7, 8]
    only_big = ep.make_threshold_filter(10)
    assert only_big([3, 10, 12]) == [10, 12]


def test_ep05_map_filter_reduce_equivalence() -> None:
    ep = load_module("ko/05-map-filter-reduce.py", "ep05")
    values = [1, 2, 3, 4, 5, 6]
    assert ep.map_filter_reduce_total(values) == ep.comprehension_total(values)


def test_ep06_closure_and_partial() -> None:
    ep = load_module("ko/06-closure-and-partial.py", "ep06")
    assert ep.make_multiplier(4)(5) == 20
    assert ep.times_three()(7) == 21


def test_ep07_recursion_and_tail_aware() -> None:
    ep = load_module("ko/07-recursion.py", "ep07")
    tree = {
        "value": 10,
        "children": [{"value": 5, "children": []}, {"value": 2, "children": []}],
    }
    assert ep.tree_sum(tree) == 17
    assert ep.factorial_tail(6) == 720


def test_ep08_lazy_evaluation_defers() -> None:
    ep = load_module("ko/08-lazy-evaluation.py", "ep08")
    counter = common.SideEffectCounter()
    stream = ep.lazy_prices(counter)
    assert counter.calls == 0
    first = next(stream)
    assert first == 1080
    assert counter.calls == 1


def test_ep09_composition_associative() -> None:
    ep = load_module("ko/09-function-composition.py", "ep09")
    left = common.compose(common.compose(ep.f, ep.g), ep.h)(10)
    right = common.compose(ep.f, common.compose(ep.g, ep.h))(10)
    assert left == right == ep.composed_value(10)


def test_ep10_oop_fp_hybrid_equal_results() -> None:
    ep = load_module("ko/10-oop-and-fp-balance.py", "ep10")
    items = [{"price": 1000, "qty": 2}, {"price": 500, "qty": 3}]
    cart = ep.Cart(items=items)
    assert cart.total() == ep.total_fp(items) == ep.total_hybrid(cart)
