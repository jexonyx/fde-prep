"""06 — counter-class. First pass in plain text (see ../../CONSTRAINTS.md)."""


class Counter:
    """Counts hashable keys. 0 means absent."""

    def __init__(self):
        raise NotImplementedError

    def increment(self, key):
        """Add 1 to key's count."""
        raise NotImplementedError

    def decrement(self, key):
        """Subtract 1; remove the key when it reaches 0; no-op if absent."""
        raise NotImplementedError

    def count(self, key):
        """Current count for key, or 0 if absent."""
        raise NotImplementedError

    def most_common(self, n=None):
        """List of (key, count) tuples, highest first; top n if given, else all.
        Ties are broken by insertion order (follow-up)."""
        raise NotImplementedError
