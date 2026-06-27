"""Reference — 13 rate-limiter. Check AFTER attempting."""
import time


class RateLimiter:
    def __init__(self, limit, window, clock=time.time):
        self.limit = limit
        self.window = window
        self._clock = clock
        self._fixed = {}    # user -> (window_index, count)
        self._sliding = {}  # user -> list of allowed timestamps

    def allow(self, user_id):
        now = self._clock()
        window_index = int(now // self.window)
        idx, count = self._fixed.get(user_id, (window_index, 0))
        if idx != window_index:        # entered a new window -> reset
            idx, count = window_index, 0
        if count < self.limit:
            self._fixed[user_id] = (idx, count + 1)
            return True
        self._fixed[user_id] = (idx, count)
        return False

    def allow_sliding(self, user_id):
        now = self._clock()
        cutoff = now - self.window
        stamps = [t for t in self._sliding.get(user_id, []) if t > cutoff]
        if len(stamps) < self.limit:
            stamps.append(now)
            self._sliding[user_id] = stamps
            return True
        self._sliding[user_id] = stamps
        return False
