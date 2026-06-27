"""13 — rate-limiter. First pass in plain text (see ../../CONSTRAINTS.md)."""
import time


class RateLimiter:
    """Per-user rate limiter. Fixed window by default; sliding window as a follow-up."""

    def __init__(self, limit, window, clock=time.time):
        """limit: max allowed calls per window. window: window length. clock: zero-arg time."""
        raise NotImplementedError

    def allow(self, user_id):
        """Fixed window: True if under the per-window limit (and record it), else False."""
        raise NotImplementedError

    def allow_sliding(self, user_id):
        """Follow-up. Sliding window over (now - window, now]."""
        raise NotImplementedError
