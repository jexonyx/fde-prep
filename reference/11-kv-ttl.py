"""Reference — 11 kv-ttl. Check AFTER attempting."""
import time

_MISSING = object()


class KVStoreTTL:
    def __init__(self, clock=time.time):
        self._clock = clock
        self._data = {}  # key -> (value, expires_at or None)

    def set(self, key, value, ttl=None):
        expires_at = None if ttl is None else self._clock() + ttl
        self._data[key] = (value, expires_at)

    def _is_expired(self, key):
        _value, expires_at = self._data[key]
        return expires_at is not None and self._clock() >= expires_at

    def _live(self, key):
        """True if present and unexpired; lazily evicts if expired."""
        if key not in self._data:
            return False
        if self._is_expired(key):
            del self._data[key]
            return False
        return True

    def get(self, key, default=_MISSING):
        if self._live(key):
            return self._data[key][0]
        if default is _MISSING:
            raise KeyError(key)
        return default

    def exists(self, key):
        return self._live(key)

    def delete(self, key):
        if not self._live(key):
            raise KeyError(key)
        del self._data[key]

    def cleanup(self):
        expired = [k for k in list(self._data) if self._is_expired(k)]
        for k in expired:
            del self._data[k]
        return len(expired)
