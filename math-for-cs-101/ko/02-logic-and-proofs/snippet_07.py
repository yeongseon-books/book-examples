"""Generated from book-content article."""

def prefix_sum(arr):
    out = []
    total = 0
    for x in arr:
        total += x
        out.append(total)
    return out
