"""Gate for the OOP exercises. Run: pytest test_primer.py"""
from exercises import Point, Tally


def test_point_stores_fields():
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2


def test_point_repr():
    assert repr(Point(1, 2)) == "Point(1, 2)"


def test_point_value_equality():
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(1, 3)


def test_point_hashable():
    assert len({Point(1, 2), Point(1, 2)}) == 1
    assert {Point(0, 0): "origin"}[Point(0, 0)] == "origin"


def test_tally_counts():
    t = Tally()
    assert t.count("a") == 0
    t.add("a")
    t.add("a")
    t.add("b")
    assert t.count("a") == 2
    assert t.count("b") == 1


def test_tally_instances_independent():
    t1, t2 = Tally(), Tally()
    t1.add("x")
    assert t2.count("x") == 0
