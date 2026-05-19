from ko import _09_container_vs_vm as ep


def test_vm_overhead_higher_than_container():
    stats = ep.simulate_overhead(container_count=5, vm_count=5)
    assert stats["vm_total_startup_ms"] > stats["container_total_startup_ms"]
    assert stats["vm_total_memory_mb"] > stats["container_total_memory_mb"]


def test_comparison_table_shape():
    table = ep.comparison_table(3, 2)
    assert table[0][0] == "startup_ms"
    assert len(table) == 2
