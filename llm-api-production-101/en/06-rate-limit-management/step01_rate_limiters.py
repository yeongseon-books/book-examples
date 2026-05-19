import os
import threading
import time
from collections import deque

from groq import Groq


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        self._capacity = capacity
        self._tokens = float(capacity)
        self._rate = refill_rate
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_refill = now

    def acquire(self, tokens: int = 1, timeout: float = 5.0) -> bool:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            with self._lock:
                self._refill()
                if self._tokens >= tokens:
                    self._tokens -= tokens
                    return True
            time.sleep(0.05)
        return False


class SlidingWindowLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self._max = max_requests
        self._window = window_seconds
        self._timestamps: deque[float] = deque()
        self._lock = threading.Lock()

    def acquire(self) -> bool:
        now = time.monotonic()
        with self._lock:
            cutoff = now - self._window
            while self._timestamps and self._timestamps[0] < cutoff:
                self._timestamps.popleft()
            if len(self._timestamps) >= self._max:
                return False
            self._timestamps.append(now)
            return True


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    bucket = TokenBucket(capacity=5, refill_rate=2.0)

    for index in range(3):
        if bucket.acquire(tokens=1):
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": f"Question {index + 1}: what is a Python f-string?",
                    }
                ],
                temperature=0.0,
            )
            content = completion.choices[0].message.content or ""
            print(f"[{index + 1}] {content[:60]}")
        else:
            print(f"[{index + 1}] Skipped because of the rate limiter.")

    window = SlidingWindowLimiter(max_requests=3, window_seconds=5.0)
    for index in range(5):
        allowed = window.acquire()
        status = "allowed" if allowed else "blocked"
        print(f"sliding window request {index + 1}: {status}")


if __name__ == "__main__":
    main()
