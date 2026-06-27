"""11 — kv-ttl. First pass in plain text (see ../../CONSTRAINTS.md)."""
import time

_MISSING = object()


class KVStoreTTL:
    """Key/value store with optional per-entry time-to-live expiry."""

    def __init__(self, clock=time.time):
        """clock: a zero-arg callable returning 'now' (injected so time is testable)."""
        raise NotImplementedError

    def set(self, key, value, ttl=None):
        """Store value; expires ttl units from now, or never if ttl is None."""
        raise NotImplementedError

    def get(self, key, default=_MISSING):
        """Value if present and unexpired; else KeyError (or default if supplied)."""
        raise NotImplementedError

    def exists(self, key):
        """True only if present and unexpired."""
        raise NotImplementedError

    def delete(self, key):
        """Remove key; KeyError if absent or already expired."""
        raise NotImplementedError

    def cleanup(self):
        """Follow-up. Actively remove all expired entries; return how many were removed."""
        raise NotImplementedError
