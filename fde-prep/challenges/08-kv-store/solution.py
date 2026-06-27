"""08 — kv-store. First pass in plain text (see ../../CONSTRAINTS.md)."""

_MISSING = object()  # sentinel for "no default supplied" (see get's follow-up)


class KVStore:
    """In-memory key/value store with explicit absent-key semantics."""

    def __init__(self):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def get(self, key, default=_MISSING):
        """Return the stored value. If key is absent: raise KeyError, unless a default was
        passed, in which case return it (without inserting it)."""
        raise NotImplementedError

    def delete(self, key):
        """Remove key. Raises KeyError if absent."""
        raise NotImplementedError

    def exists(self, key):
        raise NotImplementedError
