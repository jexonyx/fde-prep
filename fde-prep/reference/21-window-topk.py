"""Reference — 21 window-topk. Check AFTER attempting."""
from collections import deque


class WindowTopK:
    def __init__(self, window_size, k):
        self.window_size = window_size
        self.k = k
        self._window = deque()  # the last window_size items, oldest at the left
        self._counts = {}       # item -> count within the window

    def add(self, item):
        self._window.append(item)
        self._counts[item] = self._counts.get(item, 0) + 1
        if len(self._window) > self.window_size:
            oldest = self._window.popleft()
            self._counts[oldest] -= 1
            if self._counts[oldest] == 0:
                del self._counts[oldest]  # don't let stale items linger

    def top_k(self):
        ranked = sorted(self._counts.items(), key=lambda kv: (-kv[1], kv[0]))
        return ranked[:self.k]
