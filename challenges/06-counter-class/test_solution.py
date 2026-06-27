from solution import Counter


class TestBasic:
    def test_increment_and_count(self):
        c = Counter()
        c.increment("a")
        c.increment("a")
        c.increment("b")
        assert c.count("a") == 2
        assert c.count("b") == 1

    def test_most_common_top_one(self):
        c = Counter()
        for k in ["a", "a", "a", "b", "b", "c"]:
            c.increment(k)
        assert c.most_common(1) == [("a", 3)]

    def test_most_common_all(self):
        c = Counter()
        for k in ["a", "a", "b"]:
            c.increment(k)
        assert c.most_common() == [("a", 2), ("b", 1)]


class TestEdge:
    def test_count_absent_is_zero(self):
        assert Counter().count("nope") == 0

    def test_decrement_removes_at_zero(self):
        c = Counter()
        c.increment("b")
        c.decrement("b")
        assert c.count("b") == 0
        assert c.most_common() == []

    def test_decrement_absent_is_noop(self):
        c = Counter()
        c.decrement("ghost")  # must not raise, must not go negative
        assert c.count("ghost") == 0

    def test_most_common_empty(self):
        assert Counter().most_common() == []
        assert Counter().most_common(3) == []

    def test_most_common_zero_n(self):
        c = Counter()
        c.increment("a")
        assert c.most_common(0) == []


class TestStretch:
    def test_tie_break_insertion_order(self):
        c = Counter()
        for k in ["a", "b", "c"]:  # all count 1, inserted a,b,c
            c.increment(k)
        assert c.most_common(2) == [("a", 1), ("b", 1)]

    def test_tie_break_mixed_counts(self):
        c = Counter()
        for k in ["x", "y", "z", "y", "x"]:  # x:2 (1st), y:2 (2nd), z:1
            c.increment(k)
        assert c.most_common() == [("x", 2), ("y", 2), ("z", 1)]

    def test_reinsert_goes_to_back_of_tie(self):
        c = Counter()
        c.increment("a")     # a inserted first
        c.increment("b")
        c.decrement("a")     # a removed
        c.increment("a")     # a re-inserted -> now after b
        # both count 1; b was inserted before the re-inserted a
        assert c.most_common() == [("b", 1), ("a", 1)]

    def test_decrement_floors_not_negative(self):
        c = Counter()
        c.increment("a")
        c.decrement("a")
        c.decrement("a")     # already gone; stays at 0
        assert c.count("a") == 0
