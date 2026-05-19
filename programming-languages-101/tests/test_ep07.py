from ko.ep07_memory_management import mark_and_sweep, simulate_ref_count


def test_ep07_memory_simulators():
    graph = {"a": ["b"], "b": [], "c": []}
    assert simulate_ref_count(graph)["b"] == 1
    assert mark_and_sweep(graph, ["a"]) == ["c"]
