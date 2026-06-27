"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import KVStore

if __name__ == "__main__":
    kv = KVStore()
    kv.set("name", "Ada")
    print("get('name'):", kv.get("name"))
    print("exists('age'):", kv.exists("age"))
    print("get('age', 0):", kv.get("age", 0))
    try:
        kv.get("age")
    except KeyError:
        print("get('age') raised KeyError as expected")
