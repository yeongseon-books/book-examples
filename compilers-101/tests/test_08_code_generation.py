from conftest import load_module

mod = load_module("ko/08-code-generation.py", "ep08")


def test_stack_vm_result() -> None:
    tac = ["t1 = 3", "t2 = 4", "t3 = t1 + t2"]
    bytecode = mod.tac_to_stack_bytecode(tac, "t3")
    assert mod.run_bytecode(bytecode) == 7
