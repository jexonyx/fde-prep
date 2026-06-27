"""15 — trie. First pass in plain text (see ../../CONSTRAINTS.md)."""


class Trie:
    """Prefix tree supporting insert / search / starts_with."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, word):
        raise NotImplementedError

    def search(self, word):
        """True if the exact word was inserted."""
        raise NotImplementedError

    def starts_with(self, prefix):
        """True if any inserted word has this prefix."""
        raise NotImplementedError

    def autocomplete(self, prefix):
        """Follow-up. All inserted words starting with prefix, sorted ascending."""
        raise NotImplementedError
