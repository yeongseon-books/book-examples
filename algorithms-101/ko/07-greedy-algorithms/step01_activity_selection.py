from __future__ import annotations


def activity_selection(intervals: list[tuple[int, int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[1])
    chosen = 0
    last_end = -1
    for s, e in intervals:
        if s >= last_end:
            chosen += 1
            last_end = e
    return chosen


def run() -> dict[str, object]:
    meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    return {"meetings": meetings, "max_non_overlapping": activity_selection(meetings)}


if __name__ == "__main__":
    print(run())
