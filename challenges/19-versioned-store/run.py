"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import VersionedStore

if __name__ == "__main__":
    vs = VersionedStore()
    vs.set("a", 1)
    vs.set("a", 2)
    vs.set("a", 3)
    print("latest:", vs.get("a"))
    print("version 0:", vs.get_at("a", 0))
    print("revert to v0 ->", vs.revert("a", 0))
    print("latest after revert:", vs.get("a"))
    print("history still has v2:", vs.get_at("a", 2))
