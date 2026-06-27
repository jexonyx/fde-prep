"""Reference — 20 pubsub. Check AFTER attempting."""


class PubSub:
    def __init__(self):
        self._subs = {}  # topic-pattern -> list of handlers (insertion order)

    def subscribe(self, topic, handler):
        self._subs.setdefault(topic, []).append(handler)

    def unsubscribe(self, topic, handler):
        handlers = self._subs.get(topic)
        if not handlers or handler not in handlers:
            return False
        handlers.remove(handler)
        if not handlers:
            del self._subs[topic]
        return True

    def publish(self, topic, msg):
        count = 0
        for pattern, handlers in list(self._subs.items()):
            if self._matches(pattern, topic):
                for handler in list(handlers):
                    count += 1
                    try:
                        handler(msg)
                    except Exception:
                        pass  # fault isolation: one bad handler can't break the rest
        return count

    @staticmethod
    def _matches(pattern, topic):
        if pattern == topic:
            return True
        pat = pattern.split(".")
        top = topic.split(".")
        if len(pat) != len(top):
            return False
        return all(ps == "*" or ps == ts for ps, ts in zip(pat, top))
