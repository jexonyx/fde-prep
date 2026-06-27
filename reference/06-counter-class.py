"""Reference — 06 counter-class. Check AFTER attempting."""


class Counter:
    def __init__(self):
        self._counts = {}

    def increment(self, key):
        self._counts[key] = self._counts.get(key, 0) + 1

    def decrement(self, key):
        if key not in self._counts:
            return
        self._counts[key] -= 1
        if self._counts[key] <= 0:
            del self._counts[key]

    def count(self, key):
        return self._counts.get(key, 0)

    def most_common(self, n=None):
        # sorted() is stable, and the dict preserves insertion order, so sorting by
        # -count alone breaks ties by insertion order.
        items = sorted(self._counts.items(), key=lambda kv: -kv[1])
        return items if n is None else items[:n]
