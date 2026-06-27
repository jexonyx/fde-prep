import pytest

from solution import get_path, set_path


def sample():
    return {"a": {"b": [{"c": 42}, {"c": 7}]}, "x": 1}


class TestBasic:
    def test_shallow_key(self):
        assert get_path(sample(), "x") == 1

    def test_nested_dict(self):
        assert get_path({"a": {"b": 2}}, "a.b") == 2

    def test_through_list(self):
        assert get_path(sample(), "a.b.0.c") == 42

    def test_second_list_element(self):
        assert get_path(sample(), "a.b.1.c") == 7


class TestEdge:
    def test_missing_key_raises(self):
        with pytest.raises(KeyError):
            get_path(sample(), "a.zzz")

    def test_list_index_out_of_range_raises(self):
        with pytest.raises(KeyError):
            get_path(sample(), "a.b.5.c")

    def test_default_on_miss(self):
        assert get_path(sample(), "a.zzz", default=0) == 0

    def test_default_none_returned_not_raised(self):
        assert get_path(sample(), "nope", default=None) is None

    def test_descend_into_scalar_is_miss(self):
        with pytest.raises(KeyError):
            get_path({"a": 5}, "a.b")

    def test_present_value_wins_over_default(self):
        assert get_path(sample(), "x", default=999) == 1


class TestStretch:
    def test_set_existing_leaf(self):
        data = {"a": {"b": 1}}
        set_path(data, "a.b", 2)
        assert data["a"]["b"] == 2

    def test_set_creates_intermediate_dicts(self):
        data = {}
        set_path(data, "a.b.c", 5)
        assert data == {"a": {"b": {"c": 5}}}

    def test_set_returns_data(self):
        data = {}
        assert set_path(data, "k", 1) is data

    def test_set_into_existing_list(self):
        data = {"a": [{"c": 1}]}
        set_path(data, "a.0.c", 99)
        assert data["a"][0]["c"] == 99

    def test_set_then_get_round_trip(self):
        data = {}
        set_path(data, "deep.nested.path", "value")
        assert get_path(data, "deep.nested.path") == "value"

    def test_set_replaces_scalar_with_dict_to_continue(self):
        data = {"a": 1}
        set_path(data, "a.b", 2)
        assert data == {"a": {"b": 2}}
