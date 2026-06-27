"""09 — lru-cache. First pass in plain text (see ../../CONSTRAINTS.md)."""


class LRUCache:
    """Fixed-capacity cache that evicts the least-recently-used key."""

    def __init__(self, capacity):
        """capacity must be a positive int (else ValueError)."""
        raise NotImplementedError

    def get(self, key):
        """Return value and mark key most-recently-used. KeyError if absent."""
        raise NotImplementedError

    def put(self, key, value):
        """Insert/update key (most-recently-used). Evict LRU if over capacity."""
        raise NotImplementedError

    def __contains__(self, key):
        """Membership test that does NOT affect recency."""
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
