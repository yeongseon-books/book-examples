from __future__ import annotations


def simulate_overhead(container_count: int, vm_count: int) -> dict[str, int]:
    return {
        'container_total_startup_ms': 120 * container_count,
        'vm_total_startup_ms': 4000 * vm_count,
        'container_total_memory_mb': 40 * container_count,
        'vm_total_memory_mb': 320 * vm_count,
    }


def comparison_table(container_count: int, vm_count: int) -> list[tuple[str, int, int]]:
    stats = simulate_overhead(container_count, vm_count)
    return [
        ('startup_ms', stats['container_total_startup_ms'], stats['vm_total_startup_ms']),
        ('memory_mb', stats['container_total_memory_mb'], stats['vm_total_memory_mb']),
    ]
