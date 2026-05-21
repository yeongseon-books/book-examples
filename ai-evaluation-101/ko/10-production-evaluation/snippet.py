"""Generated from book-content article."""

def failure_biased_sample(traces, rate_pass=0.005, rate_fail=0.5):
    sampled = []
    for t in traces:
        threshold = rate_fail if t.get("user_feedback") == "down" else rate_pass
        if random.random() < threshold:
            sampled.append(t)
    return sampled
