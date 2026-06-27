"""14 — mini-table. First pass in plain text (see ../../CONSTRAINTS.md)."""


class MiniTable:
    """In-memory table of row dicts with an equality where-clause."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, row):
        """Store a copy of the row dict."""
        raise NotImplementedError

    def select(self, *columns, **filters):
        """Rows where every column == value in filters. No filters -> all rows.
        If positional columns are given (follow-up), project each result to those columns."""
        raise NotImplementedError

    def where(self, predicate):
        """Follow-up. Rows for which predicate(row) is truthy."""
        raise NotImplementedError
