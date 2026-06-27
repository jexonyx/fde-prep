import pytest

from solution import KVStore


class TestBasic:
    def test_set_and_get(self):
        kv = KVStore()
        kv.set("a", 1)
        assert kv.get("a") == 1

    def test_exists(self):
        kv = KVStore()
        assert kv.exists("a") is False
        kv.set("a", 1)
        assert kv.exists("a") is True

    def test_delete(self):
        kv = KVStore()
        kv.set("a", 1)
        kv.delete("a")
        assert kv.exists("a") is False


class TestEdge:
    def test_get_missing_raises(self):
        with pytest.raises(KeyError):
            KVStore().get("nope")

    def test_delete_missing_raises(self):
        with pytest.raises(KeyError):
            KVStore().delete("nope")

    def test_overwrite(self):
        kv = KVStore()
        kv.set("a", 1)
        kv.set("a", 2)
        assert kv.get("a") == 2

    def test_none_is_a_valid_value(self):
        kv = KVStore()
        kv.set("a", None)
        assert kv.exists("a") is True
        assert kv.get("a") is None


class TestStretch:
    def test_get_with_default_on_missing(self):
        kv = KVStore()
        assert kv.get("missing", 99) == 99

    def test_default_none_distinct_from_missing(self):
        kv = KVStore()
        # default of None must be returned, not raise
        assert kv.get("missing", None) is None

    def test_default_not_inserted(self):
        kv = KVStore()
        kv.get("ghost", 0)
        assert kv.exists("ghost") is False

    def test_get_with_default_returns_real_value_when_present(self):
        kv = KVStore()
        kv.set("a", 1)
        assert kv.get("a", 99) == 1

    def test_get_stored_none_with_default(self):
        kv = KVStore()
        kv.set("a", None)
        # key exists with value None -> return None, NOT the default
        assert kv.get("a", 99) is None
