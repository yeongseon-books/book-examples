"""Generated from book-content article."""

import heapq


def huffman_lengths(freqs):
    heap = [[f, [s, ""]] for s, f in freqs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return {s: len(code) for s, code in heap[0][1:]}

print(huffman_lengths({'A':45,'B':13,'C':12,'D':16,'E':9,'F':5}))
