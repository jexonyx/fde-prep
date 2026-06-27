"""12 — event-log. First pass in plain text (see ../../CONSTRAINTS.md)."""


class EventLog:
    """Append-only log of (timestamp, type, payload) events with simple queries."""

    def __init__(self):
        raise NotImplementedError

    def append(self, timestamp, event_type, payload):
        raise NotImplementedError

    def by_type(self, event_type):
        """Events of event_type, in insertion order, as (timestamp, type, payload) tuples."""
        raise NotImplementedError

    def in_range(self, start, end):
        """Events with start <= timestamp <= end (inclusive), in insertion order."""
        raise NotImplementedError

    def count_by_type(self):
        """Follow-up. dict of event_type -> count."""
        raise NotImplementedError

    def query(self, event_type=None, start=None, end=None):
        """Follow-up. Combined filter; a None argument means 'don't filter on this'."""
        raise NotImplementedError
