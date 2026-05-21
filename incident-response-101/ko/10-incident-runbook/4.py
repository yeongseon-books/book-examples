"""Generated from book-content article."""

STEPS = ("ack", "stabilize", "communicate", "investigate", "resolve")

def next_step(current):
    i = STEPS.index(current)
    return STEPS[i + 1] if i + 1 < len(STEPS) else "done"
