"""Reference — 09 lru-cache. Check AFTER attempting."""


class LRUCache:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive int")
        self.capacity = capacity
        self._data = {}  # insertion order == LRU (front) -> MRU (back)

    def get(self, key):
        if key not in self._data:
            raise KeyError(key)
        value = self._data.pop(key)
        self._data[key] = value  # reinsert at the MRU end
        return value

    def put(self, key, value):
        if key in self._data:
            self._data.pop(key)  # so reinsert refreshes recency
        self._data[key] = value
        if len(self._data) > self.capacity:
            lru_key = next(iter(self._data))  # first = least-recently-used
            del self._data[lru_key]

    def __contains__(self, key):
        return key in self._data  # no recency change

    def __len__(self):
        return len(self._data)
