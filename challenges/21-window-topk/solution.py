"""21 — window-topk. First pass in plain text (see ../../CONSTRAINTS.md)."""


class WindowTopK:
    """Top-K most frequent items within a sliding window of the last `window_size` events."""

    def __init__(self, window_size, k):
        raise NotImplementedError

    def add(self, item):
        """Record item as newest; evict the oldest if the window is over capacity."""
        raise NotImplementedError

    def top_k(self):
        """Up to k (item, count) tuples, count descending, ties broken by item ascending."""
        raise NotImplementedError
