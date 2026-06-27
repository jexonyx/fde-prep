import pytest

from solution import KVStoreTTL


class FakeClock:
    """A controllable clock: callable, with advance()."""
    def __init__(self, t=0):
        self.t = t

    def __call__(self):
        return self.t

    def advance(self, delta):
        self.t += delta


class TestBasic:
    def test_set_get_no_ttl(self):
        kv = KVStoreTTL(clock=FakeClock(0))
        kv.set("a", 1)
        assert kv.get("a") == 1

    def test_get_before_expiry(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=10)
        clock.advance(5)
        assert kv.get("a") == 1

    def test_exists(self):
        kv = KVStoreTTL(clock=FakeClock(0))
        kv.set("a", 1, ttl=10)
        assert kv.exists("a") is True


class TestEdge:
    def test_expires_at_boundary(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=10)
        clock.advance(10)              # now == expires_at -> expired
        with pytest.raises(KeyError):
            kv.get("a")

    def test_exists_false_after_expiry(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=5)
        clock.advance(6)
        assert kv.exists("a") is False

    def test_none_ttl_never_expires(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1)
        clock.advance(10_000)
        assert kv.get("a") == 1

    def test_overwrite_resets_ttl(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=10)
        clock.advance(9)
        kv.set("a", 2, ttl=10)        # reset: now expires at 19
        clock.advance(9)              # now == 18 < 19
        assert kv.get("a") == 2

    def test_delete_expired_raises(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=5)
        clock.advance(10)
        with pytest.raises(KeyError):
            kv.delete("a")


class TestStretch:
    def test_get_with_default_after_expiry(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=5)
        clock.advance(6)
        assert kv.get("a", 99) == 99

    def test_cleanup_returns_count_and_removes(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=5)
        kv.set("b", 2, ttl=20)
        kv.set("c", 3)                # permanent
        clock.advance(10)             # only "a" expired
        removed = kv.cleanup()
        assert removed == 1
        assert kv.exists("a") is False
        assert kv.get("b") == 2
        assert kv.get("c") == 3

    def test_lazy_expiry_drops_on_read(self):
        clock = FakeClock(0)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=5)
        clock.advance(6)
        # touching the key lazily evicts it; a later cleanup finds nothing to do
        assert kv.exists("a") is False
        assert kv.cleanup() == 0

    def test_ttl_zero_expires_immediately(self):
        clock = FakeClock(100)
        kv = KVStoreTTL(clock=clock)
        kv.set("a", 1, ttl=0)
        with pytest.raises(KeyError):
            kv.get("a")
