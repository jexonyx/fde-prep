from solution import EventLog


def make_log():
    log = EventLog()
    log.append(1, "click", {"x": 10})
    log.append(2, "view", {"page": "home"})
    log.append(3, "click", {"x": 20})
    return log


class TestBasic:
    def test_by_type(self):
        log = make_log()
        assert log.by_type("click") == [
            (1, "click", {"x": 10}),
            (3, "click", {"x": 20}),
        ]

    def test_in_range(self):
        log = make_log()
        assert log.in_range(2, 3) == [
            (2, "view", {"page": "home"}),
            (3, "click", {"x": 20}),
        ]

    def test_by_type_single(self):
        log = make_log()
        assert log.by_type("view") == [(2, "view", {"page": "home"})]


class TestEdge:
    def test_empty_log(self):
        log = EventLog()
        assert log.by_type("x") == []
        assert log.in_range(0, 100) == []

    def test_type_not_present(self):
        assert make_log().by_type("purchase") == []

    def test_range_inclusive_boundaries(self):
        log = make_log()
        assert log.in_range(1, 1) == [(1, "click", {"x": 10})]
        assert log.in_range(3, 3) == [(3, "click", {"x": 20})]

    def test_range_no_match(self):
        assert make_log().in_range(10, 20) == []

    def test_insertion_order_with_unsorted_timestamps(self):
        log = EventLog()
        log.append(5, "a", 1)
        log.append(1, "a", 2)
        # results follow insertion order, not timestamp order
        assert log.by_type("a") == [(5, "a", 1), (1, "a", 2)]


class TestStretch:
    def test_count_by_type(self):
        assert make_log().count_by_type() == {"click": 2, "view": 1}

    def test_count_by_type_empty(self):
        assert EventLog().count_by_type() == {}

    def test_query_type_only(self):
        assert make_log().query(event_type="click") == make_log().by_type("click")

    def test_query_range_only(self):
        assert make_log().query(start=2, end=3) == make_log().in_range(2, 3)

    def test_query_combined(self):
        log = make_log()
        # clicks in [3, 99] -> only the t=3 click
        assert log.query(event_type="click", start=3, end=99) == [
            (3, "click", {"x": 20}),
        ]

    def test_query_no_filters_returns_all(self):
        log = make_log()
        assert log.query() == [
            (1, "click", {"x": 10}),
            (2, "view", {"page": "home"}),
            (3, "click", {"x": 20}),
        ]

    def test_query_open_ended_start(self):
        log = make_log()
        assert log.query(end=2) == [
            (1, "click", {"x": 10}),
            (2, "view", {"page": "home"}),
        ]
