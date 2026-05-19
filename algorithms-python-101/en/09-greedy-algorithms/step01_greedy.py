def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected: list[tuple[int, int]] = []
    last_end = 0
    for start, end in sorted_acts:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


if __name__ == "__main__":
    sample = [(1, 4), (3, 5), (5, 7), (8, 11), (12, 16)]
    print(activity_selection(sample))
