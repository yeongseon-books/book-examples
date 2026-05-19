from ko.ep07_memory_management import simulate_ref_count, mark_and_sweep

def test_ep07_memory_simulators():
    graph = {"a": ["b"], "b": [], "c": []}
    assert simulate_ref_count(graph)["b"] == 1
    assert mark_and_sweep(graph, ["a"]) == ["c"]
