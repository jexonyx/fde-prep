import pytest

from solution import MinStack


class TestBasic:
    def test_push_top_min(self):
        s = MinStack()
        s.push(3)
        s.push(1)
        s.push(2)
        assert s.top() == 2
        assert s.get_min() == 1

    def test_pop_returns_top(self):
        s = MinStack()
        s.push(5)
        s.push(9)
        assert s.pop() == 9
        assert s.top() == 5

    def test_min_recovers_after_pop(self):
        s = MinStack()
        s.push(3)
        s.push(1)
        s.pop()
        assert s.get_min() == 3


class TestEdge:
    def test_pop_empty_raises(self):
        with pytest.raises(IndexError):
            MinStack().pop()

    def test_top_empty_raises(self):
        with pytest.raises(IndexError):
            MinStack().top()

    def test_get_min_empty_raises(self):
        with pytest.raises(IndexError):
            MinStack().get_min()

    def test_empty_after_popping_everything(self):
        s = MinStack()
        s.push(1)
        s.pop()
        with pytest.raises(IndexError):
            s.get_min()

    def test_single_element(self):
        s = MinStack()
        s.push(42)
        assert s.top() == 42 and s.get_min() == 42


class TestStretch:
    def test_duplicate_minimums(self):
        s = MinStack()
        s.push(2)
        s.push(2)
        s.push(1)
        s.push(1)
        s.pop()            # remove one 1
        assert s.get_min() == 1
        s.pop()            # remove the other 1
        assert s.get_min() == 2
        s.pop()            # remove one 2
        assert s.get_min() == 2

    def test_interleaved_sequence(self):
        s = MinStack()
        seq = [5, 3, 7, 3, 8, 1]
        for x in seq:
            s.push(x)
        assert s.get_min() == 1
        assert s.pop() == 1
        assert s.get_min() == 3
        assert s.pop() == 8
        assert s.get_min() == 3
        assert s.pop() == 3
        assert s.get_min() == 3

    def test_negatives(self):
        s = MinStack()
        s.push(-1)
        s.push(-5)
        s.push(0)
        assert s.get_min() == -5
