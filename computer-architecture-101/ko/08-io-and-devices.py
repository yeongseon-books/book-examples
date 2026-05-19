from __future__ import annotations


def simulate_polling(total_ticks: int, ready_tick: int) -> dict[str, int]:
    checks = 0
    work_done = 0
    for tick in range(total_ticks):
        checks += 1
        if tick >= ready_tick:
            break
        work_done += 0
    return {"checks": checks, "work_units": work_done}


def simulate_interrupt(total_ticks: int, ready_tick: int) -> dict[str, int]:
    interrupts = 0
    work_done = 0
    for tick in range(total_ticks):
        if tick == ready_tick:
            interrupts += 1
            break
        work_done += 1
    return {"interrupts": interrupts, "work_units": work_done}


if __name__ == "__main__":
    print(simulate_polling(1000, 700))
    print(simulate_interrupt(1000, 700))
