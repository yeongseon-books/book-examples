"""Generated from book-content article."""

import time

import redis

r = redis.Redis()

def token_bucket(key: str, capacity: int, refill_per_sec: float, cost: int) -> bool:
    now = time.time()
    pipe = r.pipeline()
    pipe.hgetall(key)
    state = pipe.execute()[0]
    tokens = float(state.get(b"tokens", capacity))
    last = float(state.get(b"ts", now))
    tokens = min(capacity, tokens + (now - last) * refill_per_sec)
    if tokens < cost:
        r.hset(key, mapping={"tokens": tokens, "ts": now})
        return False
    tokens -= cost
    r.hset(key, mapping={"tokens": tokens, "ts": now})
    r.expire(key, 3600)
    return True
