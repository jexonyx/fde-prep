from solution import WindowTopK


class TestBasic:
    def test_counts_within_window(self):
        w = WindowTopK(window_size=3, k=2)
        w.add("a")
        w.add("b")
        w.add("a")
        assert w.top_k() == [("a", 2), ("b", 1)]

    def test_top_k_limit(self):
        w = WindowTopK(window_size=5, k=1)
        for item in ["a", "a", "b"]:
            w.add(item)
        assert w.top_k() == [("a", 2)]

    def test_single_item(self):
        w = WindowTopK(window_size=3, k=3)
        w.add("x")
        assert w.top_k() == [("x", 1)]


class TestEdge:
    def test_before_window_fills(self):
        w = WindowTopK(window_size=10, k=2)
        w.add("a")
        w.add("b")
        assert w.top_k() == [("a", 1), ("b", 1)]

    def test_eviction_decrements_count(self):
        w = WindowTopK(window_size=3, k=3)
        for item in ["a", "b", "a", "c"]:  # window becomes [b, a, c]
            w.add(item)
        assert w.top_k() == [("a", 1), ("b", 1), ("c", 1)]

    def test_evicted_item_disappears(self):
        w = WindowTopK(window_size=2, k=5)
        w.add("a")
        w.add("a")          # window [a, a]
        w.add("b")          # window [a, b], one "a" evicted
        w.add("b")          # window [b, b], the other "a" evicted
        assert w.top_k() == [("b", 2)]

    def test_window_size_one(self):
        w = WindowTopK(window_size=1, k=3)
        w.add("a")
        w.add("b")
        assert w.top_k() == [("b", 1)]

    def test_k_zero(self):
        w = WindowTopK(window_size=3, k=0)
        w.add("a")
        assert w.top_k() == []


class TestStretch:
    def test_tie_break_item_ascending(self):
        w = WindowTopK(window_size=4, k=4)
        for item in ["d", "c", "b", "a"]:  # all count 1
            w.add(item)
        assert w.top_k() == [("a", 1), ("b", 1), ("c", 1), ("d", 1)]

    def test_tie_break_mixed_counts(self):
        w = WindowTopK(window_size=6, k=3)
        for item in ["x", "y", "x", "z", "y", "z"]:  # x:2, y:2, z:2
            w.add(item)
        assert w.top_k() == [("x", 2), ("y", 2), ("z", 2)]

    def test_long_stream_correctness(self):
        w = WindowTopK(window_size=3, k=2)
        result = None
        for item in ["a", "a", "a", "b", "b", "c"]:
            w.add(item)
            result = w.top_k()
        # final window is the last 3: [b, b, c]
        assert result == [("b", 2), ("c", 1)]

    def test_top_k_after_full_turnover(self):
        w = WindowTopK(window_size=2, k=2)
        for item in ["a", "b", "c", "d"]:
            w.add(item)
        # window is [c, d]
        assert w.top_k() == [("c", 1), ("d", 1)]
