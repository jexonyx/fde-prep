"""OOP primer — read top to bottom, then run me: `python primer.py`.

Every section ends in `assert`s. A clean run means every class did what its comments claim.
"""

# ---------------------------------------------------------------------------
# 1. __init__ and self — the instance is just a bag of attributes
# ---------------------------------------------------------------------------
class Dog:
    def __init__(self, name):
        # `self` IS the new instance. Assigning to self.name stores per-instance state.
        self.name = name

    def speak(self):
        return f"{self.name} says woof"


rex = Dog("Rex")
assert rex.name == "Rex"
assert rex.speak() == "Rex says woof"
assert Dog("Ada").speak() == "Ada says woof"

# ---------------------------------------------------------------------------
# 2. Instance vs class attributes (and the shared-mutable-default trap)
# ---------------------------------------------------------------------------
class Counter:
    species = "counter"      # CLASS attribute — shared by every instance
    def __init__(self):
        self.value = 0       # INSTANCE attribute — one per object

a, b = Counter(), Counter()
a.value += 1
assert a.value == 1 and b.value == 0           # instance state is independent
assert a.species == b.species == "counter"     # class state is shared


class Bad:
    items = []               # TRAP: one list shared across ALL instances
class Good:
    def __init__(self):
        self.items = []      # FIX: give each instance its own list

x, y = Bad(), Bad()
x.items.append(1)
assert y.items == [1]        # surprise! they share the SAME list
p, q = Good(), Good()
p.items.append(1)
assert q.items == []         # correct: independent lists
# Lesson: mutable defaults (lists/dicts/sets) belong in __init__, never as class attributes.

# ---------------------------------------------------------------------------
# 3. Methods, and returning self for chaining
# ---------------------------------------------------------------------------
class Builder:
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
        return self          # returning self lets callers chain
    def result(self):
        return "-".join(self.parts)

assert Builder().add("a").add("b").add("c").result() == "a-b-c"

# ---------------------------------------------------------------------------
# 4. __repr__ — make your objects debuggable
# ---------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        # Aim for an unambiguous, ideally eval-able string. This is what shows up in the
        # debugger, in test failure messages, and when you print a list of objects.
        return f"Point({self.x}, {self.y})"

assert repr(Point(1, 2)) == "Point(1, 2)"
assert f"{[Point(1, 2)]}" == "[Point(1, 2)]"   # repr is used inside containers

# ---------------------------------------------------------------------------
# 5. __eq__ AND __hash__ — they must agree
# ---------------------------------------------------------------------------
# By default objects compare by identity (is), not by value. To compare by value, define
# __eq__. The RULE: if a == b then hash(a) == hash(b). So if you define __eq__ and still want
# the object usable in sets/dict keys, define __hash__ over the SAME fields.
class Coord:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Coord) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))     # hash the same fields __eq__ compares

assert Coord(1, 2) == Coord(1, 2)              # value equality
assert Coord(1, 2) != Coord(1, 3)
assert len({Coord(1, 2), Coord(1, 2)}) == 1    # equal objects collapse in a set
assert {Coord(0, 0): "origin"}[Coord(0, 0)] == "origin"   # usable as a dict key

# ---------------------------------------------------------------------------
# 6. Why tuples are hashable and make great dict keys
# ---------------------------------------------------------------------------
# A tuple of hashable things is itself hashable (immutable -> stable hash). A list is NOT
# hashable (mutable). So tuples are the natural composite key — grid coordinates, (row, col),
# a sorted-letter signature for anagrams, etc.
grid = {}
grid[(0, 0)] = "start"
grid[(1, 2)] = "treasure"
assert grid[(1, 2)] == "treasure"
try:
    {}[[1, 2]] = "x"          # lists can't be keys
    assert False, "should have raised"
except TypeError:
    pass
# Anagram signature trick used in challenge 03:
sig = tuple(sorted("listen"))
assert sig == tuple(sorted("silent"))   # same signature -> same dict bucket

# ---------------------------------------------------------------------------
# 7. @dataclass — when it saves the boilerplate
# ---------------------------------------------------------------------------
# A dataclass auto-generates __init__, __repr__, and __eq__ from the annotated fields.
# Reach for it when a class is mostly "hold these fields"; write methods by hand when there's
# real behaviour. (frozen=True also makes it hashable/immutable.)
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    qty: int = 0           # field with a default

i = Item("pen", 3)
assert i.name == "pen" and i.qty == 3
assert Item("pen", 3) == Item("pen", 3)       # __eq__ for free
assert repr(Item("pen", 3)) == "Item(name='pen', qty=3)"
assert Item("pen").qty == 0                    # default applied

@dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int
assert hash(FrozenPoint(1, 2)) == hash(FrozenPoint(1, 2))   # frozen -> hashable

# ---------------------------------------------------------------------------
# 8. Raising and catching exceptions cleanly
# ---------------------------------------------------------------------------
def get_or_raise(d, key):
    if key not in d:
        raise KeyError(key)       # signal "absent" with the right exception type
    return d[key]

assert get_or_raise({"a": 1}, "a") == 1
try:
    get_or_raise({}, "missing")
    assert False, "should have raised"
except KeyError as err:
    assert str(err) == "'missing'"

# A custom exception is just a subclass — gives callers a precise thing to catch.
class CycleError(Exception):
    """Raised when a reference cycle is detected (see challenge 16)."""

def check(cyclic):
    if cyclic:
        raise CycleError("cycle!")
    return "ok"

assert check(False) == "ok"
try:
    check(True)
    assert False
except CycleError as err:
    assert "cycle" in str(err)

if __name__ == "__main__":
    print("primer 00b — all OOP asserts passed ✓")
