"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import MiniSheet, CycleError

if __name__ == "__main__":
    s = MiniSheet()
    s.set("A1", 5)
    s.set("A2", "=A1")
    s.set("A3", "=A2")
    print("A3 resolves to:", s.get("A3"))
    s.set("B1", "=B2")
    s.set("B2", "=B1")
    try:
        s.get("B1")
    except CycleError as err:
        print("cycle detected:", err)
