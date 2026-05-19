"""에피소드 06: 스케줄러 시뮬레이터(FCFS, SJF, RR)"""

from collections import deque


def fcfs_avg_waiting(jobs: list[tuple[str, int, int]]) -> float:
    time = 0
    waiting = 0
    for _, arrival, burst in sorted(jobs, key=lambda x: x[1]):
        time = max(time, arrival)
        waiting += time - arrival
        time += burst
    return waiting / len(jobs)


def sjf_avg_waiting(jobs: list[tuple[str, int, int]]) -> float:
    jobs = sorted(jobs, key=lambda x: x[1])
    i = 0
    n = len(jobs)
    time = 0
    waiting = 0
    ready: list[tuple[int, str, int]] = []
    while i < n or ready:
        while i < n and jobs[i][1] <= time:
            name, arrival, burst = jobs[i]
            ready.append((burst, name, arrival))
            i += 1
        if not ready:
            time = jobs[i][1]
            continue
        ready.sort(key=lambda x: x[0])
        burst, _, arrival = ready.pop(0)
        waiting += time - arrival
        time += burst
    return waiting / n


def rr_avg_waiting(jobs: list[tuple[str, int, int]], quantum: int = 2) -> float:
    jobs = sorted(jobs, key=lambda x: x[1])
    remaining = {name: burst for name, _, burst in jobs}
    arrival = {name: a for name, a, _ in jobs}
    finish: dict[str, int] = {}
    q: deque[str] = deque()
    time = 0
    i = 0
    while i < len(jobs) or q:
        while i < len(jobs) and jobs[i][1] <= time:
            q.append(jobs[i][0])
            i += 1
        if not q:
            time = jobs[i][1]
            continue
        name = q.popleft()
        run = min(quantum, remaining[name])
        remaining[name] -= run
        time += run
        while i < len(jobs) and jobs[i][1] <= time:
            q.append(jobs[i][0])
            i += 1
        if remaining[name] > 0:
            q.append(name)
        else:
            finish[name] = time
    total_wait = sum(finish[name] - arrival[name] - burst for name, _, burst in jobs)
    return total_wait / len(jobs)


if __name__ == "__main__":
    sample = [("P1", 0, 8), ("P2", 1, 4), ("P3", 2, 2)]
    print("FCFS", fcfs_avg_waiting(sample))
    print("SJF ", sjf_avg_waiting(sample))
    print("RR  ", rr_avg_waiting(sample, quantum=2))
