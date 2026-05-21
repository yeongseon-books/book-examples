"""Generated from book-content article."""

import json
import time


def with_stats(stage_fn):
    def wrapper(df, *args, **kwargs):
        n_in = len(df)
        t0 = time.time()
        out = stage_fn(df, *args, **kwargs)
        n_out = len(out) if hasattr(out, "__len__") else sum(len(v) for v in out.values())
        stats = {
            "stage": stage_fn.__name__,
            "rows_in": n_in,
            "rows_out": n_out,
            "drop_rate": 1 - n_out / max(n_in, 1),
            "duration_s": round(time.time() - t0, 2),
            "ts": datetime.utcnow().isoformat(),
        }
        with open(f"stats/{stage_fn.__name__}.jsonl", "a") as f:
            f.write(json.dumps(stats) + "\n")
        return out
    return wrapper

stage_clean = with_stats(stage_clean)
