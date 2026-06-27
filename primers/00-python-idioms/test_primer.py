"""Gate for the idiom exercises. Run: pytest test_primer.py"""
from exercises import (
    reverse_string,
    drop_first_last,
    word_lengths,
    evens,
    tally,
    rank_desc,
)


def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("x") == "x"


def test_drop_first_last():
    assert drop_first_last("hello") == "ell"
    assert drop_first_last("ab") == ""


def test_word_lengths():
    assert word_lengths(["hi", "yo!"]) == {"hi": 2, "yo!": 3}
    assert word_lengths([]) == {}


def test_evens():
    assert evens([1, 2, 3, 4]) == [2, 4]
    assert evens([1, 3, 5]) == []
    assert evens([]) == []


def test_tally():
    assert tally(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert tally([]) == {}


def test_rank_desc():
    assert rank_desc({"a": 2, "b": 3, "c": 2}) == ["b", "a", "c"]
    assert rank_desc({}) == []
