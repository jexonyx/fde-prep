import pytest

from solution import LRUCache


class TestBasic:
    def test_put_get(self):
        c = LRUCache(2)
        c.put("a", 1)
        assert c.get("a") == 1

    def test_update_existing(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("a", 2)
        assert c.get("a") == 2
        assert len(c) == 1

    def test_len(self):
        c = LRUCache(3)
        c.put("a", 1)
        c.put("b", 2)
        assert len(c) == 2


class TestEdge:
    def test_get_missing_raises(self):
        with pytest.raises(KeyError):
            LRUCache(2).get("nope")

    def test_eviction_basic(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        c.put("c", 3)          # over capacity -> evict LRU "a"
        assert "a" not in c
        assert c.get("b") == 2
        assert c.get("c") == 3

    def test_capacity_one(self):
        c = LRUCache(1)
        c.put("a", 1)
        c.put("b", 2)          # evicts "a"
        assert "a" not in c
        assert c.get("b") == 2

    def test_invalid_capacity_raises(self):
        with pytest.raises(ValueError):
            LRUCache(0)
        with pytest.raises(ValueError):
            LRUCache(-3)

    def test_contains_does_not_refresh(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        assert "a" in c        # membership must NOT promote "a"
        c.put("c", 3)          # "a" is still LRU -> evicted
        assert "a" not in c
        assert "b" in c and "c" in c


class TestStretch:
    def test_get_refreshes_recency(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        assert c.get("a") == 1   # "a" now most-recent; "b" is LRU
        c.put("c", 3)            # evict "b", not "a"
        assert "b" not in c
        assert c.get("a") == 1
        assert c.get("c") == 3

    def test_put_existing_refreshes_recency(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        c.put("a", 10)          # refresh "a" -> "b" becomes LRU
        c.put("c", 3)           # evict "b"
        assert "b" not in c
        assert c.get("a") == 10

    def test_long_sequence(self):
        c = LRUCache(3)
        for k in ["a", "b", "c"]:
            c.put(k, k.upper())
        c.get("a")              # order LRU->MRU now: b, c, a
        c.put("d", "D")         # evict "b"
        assert "b" not in c
        assert sorted([k for k in ["a", "c", "d"] if k in c]) == ["a", "c", "d"]
        assert len(c) == 3
