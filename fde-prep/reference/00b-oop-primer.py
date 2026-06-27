"""Reference — completed OOP exercises. Check AFTER attempting."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Tally:
    def __init__(self):
        self.counts = {}

    def add(self, item):
        self.counts[item] = self.counts.get(item, 0) + 1

    def count(self, item):
        return self.counts.get(item, 0)
