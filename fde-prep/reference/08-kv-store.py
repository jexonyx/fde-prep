"""Reference — 08 kv-store. Check AFTER attempting."""

_MISSING = object()


class KVStore:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key, default=_MISSING):
        if key in self._data:
            return self._data[key]
        if default is _MISSING:
            raise KeyError(key)
        return default

    def delete(self, key):
        if key not in self._data:
            raise KeyError(key)
        del self._data[key]

    def exists(self, key):
        return key in self._data
