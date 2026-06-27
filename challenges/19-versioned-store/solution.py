"""19 — versioned-store. First pass in plain text (see ../../CONSTRAINTS.md)."""


class VersionedStore:
    """Key/value store that keeps every version (snapshot) of each key."""

    def __init__(self):
        raise NotImplementedError

    def set(self, key, value):
        """Record a new version of key (first is version 0)."""
        raise NotImplementedError

    def get(self, key):
        """Latest value. KeyError if key unknown."""
        raise NotImplementedError

    def get_at(self, key, version):
        """Value at a historical version. KeyError if key unknown; IndexError if version bad."""
        raise NotImplementedError

    def revert(self, key, version):
        """Follow-up. Append a new version equal to the value at `version`; return that value."""
        raise NotImplementedError
