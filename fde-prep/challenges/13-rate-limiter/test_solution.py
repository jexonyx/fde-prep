from solution import RateLimiter


class FakeClock:
    def __init__(self, t=0):
        self.t = t

    def __call__(self):
        return self.t

    def advance(self, delta):
        self.t += delta


class TestBasic:
    def test_under_limit_allowed(self):
        rl = RateLimiter(limit=2, window=10, clock=FakeClock(0))
        assert rl.allow("u") is True
        assert rl.allow("u") is True

    def test_over_limit_blocked(self):
        rl = RateLimiter(limit=2, window=10, clock=FakeClock(0))
        rl.allow("u")
        rl.allow("u")
        assert rl.allow("u") is False

    def test_users_independent(self):
        rl = RateLimiter(limit=1, window=10, clock=FakeClock(0))
        assert rl.allow("a") is True
        assert rl.allow("b") is True
        assert rl.allow("a") is False


class TestEdge:
    def test_window_resets(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=2, window=10, clock=clock)
        rl.allow("u")
        rl.allow("u")
        assert rl.allow("u") is False
        clock.advance(10)             # new window
        assert rl.allow("u") is True

    def test_rejected_does_not_consume(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=1, window=10, clock=clock)
        assert rl.allow("u") is True
        assert rl.allow("u") is False
        assert rl.allow("u") is False  # still just 1 consumed
        clock.advance(10)
        assert rl.allow("u") is True

    def test_limit_zero_always_rejects(self):
        rl = RateLimiter(limit=0, window=10, clock=FakeClock(0))
        assert rl.allow("u") is False

    def test_same_window_within_boundary(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=1, window=10, clock=clock)
        assert rl.allow("u") is True
        clock.advance(9)              # still window 0
        assert rl.allow("u") is False


class TestStretch:
    def test_sliding_basic(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=2, window=10, clock=clock)
        assert rl.allow_sliding("u") is True   # t=0
        clock.advance(5)
        assert rl.allow_sliding("u") is True   # t=5
        assert rl.allow_sliding("u") is False  # 2 in last 10

    def test_sliding_rolls_forward(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=2, window=10, clock=clock)
        rl.allow_sliding("u")          # t=0
        clock.advance(5)
        rl.allow_sliding("u")          # t=5
        clock.advance(6)               # t=11: the t=0 call is now >10 old
        assert rl.allow_sliding("u") is True   # only t=5 still counts

    def test_sliding_exact_boundary_drops_old(self):
        clock = FakeClock(0)
        rl = RateLimiter(limit=1, window=10, clock=clock)
        assert rl.allow_sliding("u") is True   # t=0
        clock.advance(10)              # t=10: the t=0 call is exactly window old -> dropped
        assert rl.allow_sliding("u") is True

    def test_sliding_independent_users(self):
        rl = RateLimiter(limit=1, window=10, clock=FakeClock(0))
        assert rl.allow_sliding("a") is True
        assert rl.allow_sliding("b") is True
        assert rl.allow_sliding("a") is False
