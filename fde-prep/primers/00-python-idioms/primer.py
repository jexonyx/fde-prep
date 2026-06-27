"""Python idioms primer — read top to bottom, then run me: `python primer.py`.

Every section ends in `assert`s. If this file runs clean, every idiom below did exactly what
its comment claims. The asserts ARE the expected output — read them.
"""

# ---------------------------------------------------------------------------
# 1. The four core containers
# ---------------------------------------------------------------------------
# list  - ordered, mutable, allows duplicates, indexable
# tuple - ordered, IMMUTABLE, allows duplicates, hashable (usable as dict key)
# dict  - key -> value, keys unique, O(1) lookup, insertion-ordered (3.7+)
# set   - unordered, unique elements, O(1) membership

nums = [3, 1, 2, 1]            # list literal
point = (10, 20)               # tuple literal — note the commas, not the parens
ages = {"ana": 30, "bo": 25}   # dict literal
seen = {1, 2, 3}               # set literal (NB: {} is an empty DICT, not a set)

assert len(nums) == 4
assert point[0] == 10 and point[1] == 20
assert ages["ana"] == 30
assert 2 in seen and 9 not in seen
assert type({}) is dict and type(set()) is set  # the empty-set gotcha

# Mutating lists / dicts / sets
nums.append(5)                 # -> [3, 1, 2, 1, 5]
ages["cy"] = 40                # add/overwrite a key
seen.add(4)
assert nums[-1] == 5           # negative index counts from the end
assert ages["cy"] == 40
assert 4 in seen

# ---------------------------------------------------------------------------
# 2. Indexing and slicing — s[start:stop:step], stop is EXCLUSIVE
# ---------------------------------------------------------------------------
s = "abcdef"
assert s[0] == "a"
assert s[-1] == "f"
assert s[1:4] == "bcd"         # indices 1,2,3
assert s[:3] == "abc"          # start defaults to 0
assert s[3:] == "def"          # stop defaults to len
assert s[::-1] == "fedcba"     # reverse via step -1 — memorise this one
assert s[1:-1] == "bcde"       # drop first and last
assert s[::2] == "ace"         # every other char
# Slicing works identically on lists:
assert [1, 2, 3, 4][1:3] == [2, 3]

# ---------------------------------------------------------------------------
# 3. dict.get, defaultdict, items()
# ---------------------------------------------------------------------------
d = {"a": 1}
assert d.get("a") == 1
assert d.get("z") is None          # missing key -> None, no KeyError
assert d.get("z", 0) == 0          # ...or your own default

# Counting pattern with get():
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
assert counts == {"b": 1, "a": 3, "n": 2}

# Same thing with defaultdict — the default is built on first access:
from collections import defaultdict
counts2 = defaultdict(int)          # int() -> 0
for ch in "banana":
    counts2[ch] += 1
assert dict(counts2) == {"b": 1, "a": 3, "n": 2}

# Iterating keys / values / pairs:
assert sorted(d.keys()) == ["a"]
assert list({"x": 1, "y": 2}.items()) == [("x", 1), ("y", 2)]

# ---------------------------------------------------------------------------
# 4. Comprehensions (list / dict / set) — and when to prefer a loop
# ---------------------------------------------------------------------------
squares = [n * n for n in range(5)]              # list comp
evens = [n for n in range(10) if n % 2 == 0]     # with a filter
lengths = {w: len(w) for w in ["hi", "yo"]}      # dict comp
uniq_lengths = {len(w) for w in ["a", "bb", "cc"]}  # set comp
assert squares == [0, 1, 4, 9, 16]
assert evens == [0, 2, 4, 6, 8]
assert lengths == {"hi": 2, "yo": 2}
assert uniq_lengths == {1, 2}
# Prefer a plain loop when the body has side effects, multiple statements, or is hard to
# read on one line. Comprehensions are for "build a new collection from an old one."

# ---------------------------------------------------------------------------
# 5. f-strings
# ---------------------------------------------------------------------------
name, score = "Ada", 0.5
assert f"{name} scored {score}" == "Ada scored 0.5"
assert f"{score:.0%}" == "50%"          # format spec after the colon
assert f"{7:03d}" == "007"              # zero-pad to width 3

# ---------------------------------------------------------------------------
# 6. enumerate, zip, unpacking
# ---------------------------------------------------------------------------
pairs = list(enumerate(["a", "b"]))          # index + value
assert pairs == [(0, "a"), (1, "b")]
assert list(enumerate(["a"], start=1)) == [(1, "a")]

zipped = list(zip([1, 2, 3], ["a", "b", "c"]))
assert zipped == [(1, "a"), (2, "b"), (3, "c")]   # stops at the shortest

a, b = (1, 2)                 # tuple unpacking
first, *rest = [1, 2, 3, 4]   # star captures the remainder as a list
assert a == 1 and b == 2
assert first == 1 and rest == [2, 3, 4]
# Unpacking in a loop is the idiomatic way to read pairs:
total = 0
for _idx, val in enumerate([10, 20]):
    total += val
assert total == 30

# ---------------------------------------------------------------------------
# 7. sorted with key= and reverse=
# ---------------------------------------------------------------------------
words = ["banana", "kiwi", "fig"]
assert sorted(words) == ["banana", "fig", "kiwi"]            # lexicographic
assert sorted(words, key=len) == ["fig", "kiwi", "banana"]   # by length
assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]
# Sort by a tuple to get tie-breaks: primary by -count, secondary by word.
scored = {"a": 2, "b": 3, "c": 2}
ranked = sorted(scored, key=lambda k: (-scored[k], k))
assert ranked == ["b", "a", "c"]   # b highest; a before c on the count tie (alpha)

# ---------------------------------------------------------------------------
# 8. Common string methods
# ---------------------------------------------------------------------------
assert "a,b,c".split(",") == ["a", "b", "c"]
assert "a b  c".split() == ["a", "b", "c"]    # no-arg split collapses whitespace
assert "-".join(["a", "b", "c"]) == "a-b-c"
assert "  hi  ".strip() == "hi"
assert "Hello".lower() == "hello"
assert "123".isdigit() and not "12a".isdigit()
assert "Hello".startswith("He") and "Hello".endswith("lo")

# ---------------------------------------------------------------------------
# 9. Truthiness and empty-collection gotchas
# ---------------------------------------------------------------------------
# Empty containers, 0, "", and None are all falsy.
assert not []
assert not {}
assert not ""
assert not 0
assert [1] and {"k": 1} and "x"     # non-empty / non-zero are truthy
# So the idiomatic "is this empty?" check is just the value itself:
items = []
assert (len(items) == 0) == (not items)
# Gotcha: `if x:` treats 0 and None the same. When 0 is a valid value, test `if x is None:`.

# ---------------------------------------------------------------------------
# 10. Membership: dict/set O(1) vs list O(n)
# ---------------------------------------------------------------------------
big_list = list(range(1000))
big_set = set(big_list)
assert 999 in big_list      # works, but scans up to n elements
assert 999 in big_set       # hashes once — O(1), regardless of size
assert "a" in {"a": 1}      # `in` on a dict checks KEYS
# Rule of thumb: if you repeatedly ask "have I seen X?", reach for a set or dict, not a list.

if __name__ == "__main__":
    print("primer 00 — all idiom asserts passed ✓")
