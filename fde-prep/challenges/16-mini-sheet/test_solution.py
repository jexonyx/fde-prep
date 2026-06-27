import pytest

from solution import MiniSheet, CycleError


class TestBasic:
    def test_literal_number(self):
        s = MiniSheet()
        s.set("A1", 5)
        assert s.get("A1") == 5

    def test_literal_string(self):
        s = MiniSheet()
        s.set("A2", "hello")
        assert s.get("A2") == "hello"

    def test_overwrite(self):
        s = MiniSheet()
        s.set("A1", 1)
        s.set("A1", 2)
        assert s.get("A1") == 2


class TestEdge:
    def test_get_unset_raises(self):
        with pytest.raises(KeyError):
            MiniSheet().get("Z9")

    def test_zero_and_falsey_literals(self):
        s = MiniSheet()
        s.set("A1", 0)
        s.set("A2", "")
        assert s.get("A1") == 0
        assert s.get("A2") == ""


class TestStretch:
    def test_single_reference(self):
        s = MiniSheet()
        s.set("A1", 5)
        s.set("A2", "=A1")
        assert s.get("A2") == 5

    def test_reference_chain(self):
        s = MiniSheet()
        s.set("A3", 7)
        s.set("A2", "=A3")
        s.set("A1", "=A2")
        assert s.get("A1") == 7

    def test_reference_to_unset_cell_raises(self):
        s = MiniSheet()
        s.set("A1", "=A2")  # A2 never set
        with pytest.raises(KeyError):
            s.get("A1")

    def test_self_reference_cycle(self):
        s = MiniSheet()
        s.set("A1", "=A1")
        with pytest.raises(CycleError):
            s.get("A1")

    def test_two_cell_cycle(self):
        s = MiniSheet()
        s.set("A1", "=A2")
        s.set("A2", "=A1")
        with pytest.raises(CycleError):
            s.get("A1")

    def test_longer_cycle(self):
        s = MiniSheet()
        s.set("A1", "=A2")
        s.set("A2", "=A3")
        s.set("A3", "=A1")
        with pytest.raises(CycleError):
            s.get("A2")

    def test_breaking_a_cycle_with_a_literal(self):
        s = MiniSheet()
        s.set("A1", "=A2")
        s.set("A2", "=A1")
        s.set("A2", 42)        # break the cycle
        assert s.get("A1") == 42

    def test_reference_resolves_after_target_set(self):
        s = MiniSheet()
        s.set("A1", "=A2")
        s.set("A2", 9)
        assert s.get("A1") == 9
