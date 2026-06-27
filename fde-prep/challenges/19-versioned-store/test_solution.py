import pytest

from solution import VersionedStore


class TestBasic:
    def test_set_get_latest(self):
        vs = VersionedStore()
        vs.set("a", 1)
        vs.set("a", 2)
        assert vs.get("a") == 2

    def test_get_at_versions(self):
        vs = VersionedStore()
        vs.set("a", 1)
        vs.set("a", 2)
        assert vs.get_at("a", 0) == 1
        assert vs.get_at("a", 1) == 2

    def test_independent_keys(self):
        vs = VersionedStore()
        vs.set("a", 1)
        vs.set("b", 9)
        assert vs.get("a") == 1 and vs.get("b") == 9


class TestEdge:
    def test_get_unknown_key(self):
        with pytest.raises(KeyError):
            VersionedStore().get("nope")

    def test_get_at_unknown_key(self):
        with pytest.raises(KeyError):
            VersionedStore().get_at("nope", 0)

    def test_get_at_bad_version(self):
        vs = VersionedStore()
        vs.set("a", 1)
        with pytest.raises(IndexError):
            vs.get_at("a", 5)

    def test_get_at_negative_version(self):
        vs = VersionedStore()
        vs.set("a", 1)
        with pytest.raises(IndexError):
            vs.get_at("a", -1)

    def test_single_version(self):
        vs = VersionedStore()
        vs.set("a", 42)
        assert vs.get("a") == 42
        assert vs.get_at("a", 0) == 42


class TestStretch:
    def test_revert_appends_new_version(self):
        vs = VersionedStore()
        vs.set("a", 1)        # v0
        vs.set("a", 2)        # v1
        vs.set("a", 3)        # v2
        reverted = vs.revert("a", 0)  # back to 1, as v3
        assert reverted == 1
        assert vs.get("a") == 1

    def test_revert_preserves_history(self):
        vs = VersionedStore()
        vs.set("a", 1)
        vs.set("a", 2)
        vs.set("a", 3)
        vs.revert("a", 0)
        # older versions are intact
        assert vs.get_at("a", 2) == 3
        assert vs.get_at("a", 3) == 1   # the revert snapshot

    def test_revert_then_set(self):
        vs = VersionedStore()
        vs.set("a", 10)
        vs.set("a", 20)
        vs.revert("a", 0)     # -> 10 (v2)
        vs.set("a", 30)       # v3
        assert vs.get("a") == 30
        assert vs.get_at("a", 2) == 10

    def test_revert_bad_version_raises(self):
        vs = VersionedStore()
        vs.set("a", 1)
        with pytest.raises(IndexError):
            vs.revert("a", 9)
