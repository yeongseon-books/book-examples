from conftest import load_module

mod = load_module("ko/04-registers-and-alu.py", "ep04")


def test_alu_ops_and_register_file() -> None:
    alu = mod.ALU()
    assert alu.bit_xor(0b1010, 0b1100) == 0b0110
    assert mod.demo() == 12
