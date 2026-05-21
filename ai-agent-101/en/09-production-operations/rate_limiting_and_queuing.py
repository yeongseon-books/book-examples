"""Generated from book-content article."""

from collections import deque

class RateLimiter:
    """Sliding-window rate limiter."""

    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.timestamps = deque()
        self.lock = threading.Lock()

    def acquire(self) -> bool:
        with self.lock:
            now = time.time()
            # Drop timestamps outside the window
            while self.timestamps and self.timestamps[0] < now - self.window:
                self.timestamps.popleft()

            if len(self.timestamps) >= self.max_requests:
                return False

            self.timestamps.append(now)
            return True

    def wait_and_acquire(self):
        while not self.acquire():
            time.sleep(0.1)

# Example usage
limiter = RateLimiter(max_requests=60, window_seconds=60)  # 60/minute
limiter.wait_and_acquire()
response = call_llm_api()
