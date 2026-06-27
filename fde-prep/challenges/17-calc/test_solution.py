import pytest

from solution import calc


class TestBasic:
    def test_add(self):
        assert calc("1 + 2") == 3

    def test_precedence(self):
        assert calc("2 + 3 * 4") == 14

    def test_left_associative_subtraction(self):
        assert calc("10 - 4 - 3") == 3

    def test_mixed(self):
        assert calc("2 * 3 + 4") == 10


class TestEdge:
    def test_whitespace(self):
        assert calc("  1+2 ") == 3
        assert calc("1   +   2") == 3

    def test_multi_digit(self):
        assert calc("12 + 34") == 46

    def test_division(self):
        assert calc("8 / 2") == 4

    def test_single_number(self):
        assert calc("42") == 42

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calc("1 / 0")

    def test_left_associative_division(self):
        assert calc("100 / 5 / 2") == 10


class TestStretch:
    def test_parens_override_precedence(self):
        assert calc("(2 + 3) * 4") == 20

    def test_parens_nested(self):
        assert calc("((1 + 2) * (3 + 4))") == 21

    def test_parens_mixed(self):
        assert calc("2 * (3 + 4) - 1") == 13

    def test_parens_with_division(self):
        assert calc("20 / (2 + 3)") == 4

    def test_deeply_nested(self):
        assert calc("(((1 + 1)))") == 2

    def test_parens_then_op(self):
        assert calc("(1 + 2) * (3 - 1) + 10") == 16
