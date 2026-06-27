"""Fill-in-the-blank OOP drills. Build two tiny classes, then run `pytest test_primer.py`.
The point is to type the mechanics — __init__, methods, __repr__, __eq__/__hash__.
"""


class Point:
    """A 2D point compared and hashed by value.

    Requirements (the tests check each):
      - Point(x, y) stores .x and .y
      - repr(Point(1, 2)) == "Point(1, 2)"
      - Point(1, 2) == Point(1, 2)  (value equality, not identity)
      - it can be used in a set / as a dict key (equal points collapse)
    """

    def __init__(self, x, y):
        raise NotImplementedError  # TODO: store x and y on self

    def __repr__(self):
        raise NotImplementedError  # TODO: return "Point(x, y)" using an f-string

    def __eq__(self, other):
        raise NotImplementedError  # TODO: compare (self.x, self.y) tuples

    def __hash__(self):
        raise NotImplementedError  # TODO: hash the (x, y) tuple


class Tally:
    """A minimal counter accumulator.

    Requirements:
      - starts empty
      - add(item) increments that item's count by 1
      - count(item) returns the current count (0 if never added)
    """

    def __init__(self):
        raise NotImplementedError  # TODO: give each instance its own dict

    def add(self, item):
        raise NotImplementedError  # TODO: increment the count for item

    def count(self, item):
        raise NotImplementedError  # TODO: return the count, defaulting to 0
