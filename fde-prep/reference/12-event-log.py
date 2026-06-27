"""Reference — 12 event-log. Check AFTER attempting."""


class EventLog:
    def __init__(self):
        self._events = []  # list of (timestamp, event_type, payload)

    def append(self, timestamp, event_type, payload):
        self._events.append((timestamp, event_type, payload))

    def by_type(self, event_type):
        return self.query(event_type=event_type)

    def in_range(self, start, end):
        return self.query(start=start, end=end)

    def count_by_type(self):
        counts = {}
        for _ts, etype, _payload in self._events:
            counts[etype] = counts.get(etype, 0) + 1
        return counts

    def query(self, event_type=None, start=None, end=None):
        result = []
        for ts, etype, payload in self._events:
            if event_type is not None and etype != event_type:
                continue
            if start is not None and ts < start:
                continue
            if end is not None and ts > end:
                continue
            result.append((ts, etype, payload))
        return result
