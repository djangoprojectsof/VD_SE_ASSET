import time
import threading
from collections import defaultdict


class RateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = defaultdict(list)
        self.lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        current_time = time.time()

        with self.lock:
            self.requests[user_id] = [timestamp for timestamp in self.requests[user_id]
                                      if current_time - timestamp < self.window_size]

            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

rate_limiter = RateLimiter(max_requests=5, window_size=60)
import concurrent.futures


def simulate_request(user_id):
    return rate_limiter.allow_request(user_id)



user_id = "user123"
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(simulate_request, [user_id] * 8))

print(results)
