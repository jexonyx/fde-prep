from solution import PubSub


class TestBasic:
    def test_subscribe_and_publish(self):
        ps = PubSub()
        received = []
        ps.subscribe("orders", received.append)
        count = ps.publish("orders", "order-1")
        assert received == ["order-1"]
        assert count == 1

    def test_multiple_subscribers(self):
        ps = PubSub()
        a, b = [], []
        ps.subscribe("t", a.append)
        ps.subscribe("t", b.append)
        count = ps.publish("t", "x")
        assert a == ["x"] and b == ["x"]
        assert count == 2

    def test_publish_to_no_subscribers(self):
        ps = PubSub()
        assert ps.publish("empty", "x") == 0


class TestEdge:
    def test_unsubscribe_stops_delivery(self):
        ps = PubSub()
        received = []
        ps.subscribe("t", received.append)
        ps.unsubscribe("t", received.append)
        ps.publish("t", "x")
        assert received == []

    def test_unsubscribe_returns_bool(self):
        ps = PubSub()
        received = []
        ps.subscribe("t", received.append)
        assert ps.unsubscribe("t", received.append) is True
        assert ps.unsubscribe("t", received.append) is False

    def test_unsubscribe_never_subscribed(self):
        ps = PubSub()
        assert ps.unsubscribe("ghost", lambda m: None) is False

    def test_handler_isolation(self):
        ps = PubSub()
        received = []

        def bad(msg):
            raise ValueError("boom")

        ps.subscribe("t", bad)
        ps.subscribe("t", received.append)
        # must not raise, and the good handler must still run
        count = ps.publish("t", "hi")
        assert received == ["hi"]
        assert count == 2

    def test_handlers_called_in_order(self):
        ps = PubSub()
        order = []
        ps.subscribe("t", lambda m: order.append("first"))
        ps.subscribe("t", lambda m: order.append("second"))
        ps.publish("t", None)
        assert order == ["first", "second"]


class TestStretch:
    def test_wildcard_single_segment(self):
        ps = PubSub()
        got = []
        ps.subscribe("orders.*", got.append)
        ps.publish("orders.created", "c")
        ps.publish("orders.shipped", "s")
        assert got == ["c", "s"]

    def test_wildcard_does_not_match_extra_segment(self):
        ps = PubSub()
        got = []
        ps.subscribe("orders.*", got.append)
        ps.publish("orders.created.eu", "x")
        assert got == []

    def test_wildcard_middle_segment(self):
        ps = PubSub()
        got = []
        ps.subscribe("a.*.c", got.append)
        ps.publish("a.b.c", "hit")
        ps.publish("a.x.c", "hit2")
        ps.publish("a.b.d", "miss")
        assert got == ["hit", "hit2"]

    def test_exact_and_wildcard_both_fire(self):
        ps = PubSub()
        exact, wild = [], []
        ps.subscribe("orders.created", exact.append)
        ps.subscribe("orders.*", wild.append)
        count = ps.publish("orders.created", "msg")
        assert exact == ["msg"] and wild == ["msg"]
        assert count == 2

    def test_leading_wildcard(self):
        ps = PubSub()
        got = []
        ps.subscribe("*.created", got.append)
        ps.publish("orders.created", "o")
        ps.publish("users.created", "u")
        ps.publish("orders.deleted", "x")
        assert got == ["o", "u"]
