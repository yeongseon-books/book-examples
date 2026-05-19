from conftest import load_module


mod = load_module("ko/08-io-and-devices.py", "ep08")


def test_interrupt_model_keeps_more_cpu_work() -> None:
    polling = mod.simulate_polling(total_ticks=1000, ready_tick=700)
    interrupt = mod.simulate_interrupt(total_ticks=1000, ready_tick=700)
    assert polling["checks"] == 701
    assert interrupt["work_units"] == 700
