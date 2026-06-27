"""20 — pubsub. First pass in plain text (see ../../CONSTRAINTS.md)."""


class PubSub:
    """Topic-based publish/subscribe with fault-isolated handlers."""

    def __init__(self):
        raise NotImplementedError

    def subscribe(self, topic, handler):
        """Register handler (called with one msg arg) for topic."""
        raise NotImplementedError

    def unsubscribe(self, topic, handler):
        """Remove handler from topic. Return True if removed, else False."""
        raise NotImplementedError

    def publish(self, topic, msg):
        """Call every matching handler with msg; return how many were invoked. A raising
        handler must not stop the others or propagate out. Wildcards are a follow-up."""
        raise NotImplementedError
