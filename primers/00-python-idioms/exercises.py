"""Fill-in-the-blank idiom drills. Replace each `raise NotImplementedError` with a one- or
two-line body, then run `pytest test_primer.py`. The goal is muscle memory — type the idiom.
"""


def reverse_string(s):
    """Return s reversed, using a slice. e.g. "abc" -> "cba"."""
    raise NotImplementedError  # TODO: one slice


def drop_first_last(s):
    """Return s without its first and last character, using a slice.
    e.g. "hello" -> "ell".  Assume len(s) >= 2."""
    raise NotImplementedError  # TODO: one slice


def word_lengths(words):
    """Return a dict mapping each word to its length, using a dict comprehension.
    e.g. ["hi", "yo!"] -> {"hi": 2, "yo!": 3}."""
    raise NotImplementedError  # TODO: dict comprehension


def evens(nums):
    """Return a list of just the even numbers, in order, using a list comprehension.
    e.g. [1, 2, 3, 4] -> [2, 4]."""
    raise NotImplementedError  # TODO: list comprehension with a filter


def tally(items):
    """Return a dict counting how many times each item appears.
    e.g. ["a", "b", "a"] -> {"a": 2, "b": 1}.  Use dict.get or a defaultdict."""
    raise NotImplementedError  # TODO: counting loop


def rank_desc(scores):
    """Given a {name: score} dict, return the names sorted by score descending,
    breaking ties alphabetically. e.g. {"a": 2, "b": 3, "c": 2} -> ["b", "a", "c"].
    Use sorted with a key."""
    raise NotImplementedError  # TODO: sorted(..., key=lambda ...)
