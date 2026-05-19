from dataclasses import dataclass


@dataclass
class PCB:
    pid: int
    burst_time: int
    remaining: int


def round_robin(processes: list[PCB], quantum: int) -> list[tuple[int, int]]:
    timeline: list[tuple[int, int]] = []
    queue = [PCB(p.pid, p.burst_time, p.remaining) for p in processes]
    while any(p.remaining > 0 for p in queue):
        for process in queue:
            if process.remaining <= 0:
                continue
            run_time = min(quantum, process.remaining)
            process.remaining -= run_time
            timeline.append((process.pid, run_time))
    return timeline


if __name__ == "__main__":
    procs = [PCB(1, 5, 5), PCB(2, 3, 3), PCB(3, 2, 2)]
    print(round_robin(procs, quantum=2))
