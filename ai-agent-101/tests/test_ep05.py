from conftest import load_module

module = load_module("ko/05-memory-and-state/step01_memory_state.py", "ep05")
SlidingMemory = module.SlidingMemory
checkpoint = module.checkpoint


def test_ep05_sliding_memory_and_checkpoint() -> None:
    memory = SlidingMemory(2)
    memory.add("a")
    memory.add("b")
    memory.add("c")
    assert memory.items == ["b", "c"]
    assert checkpoint({"x": 1}) == {"x": 1}
