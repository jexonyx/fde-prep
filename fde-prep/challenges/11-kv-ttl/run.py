"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import KVStoreTTL


class Clock:
    def __init__(self): self.t = 0
    def __call__(self): return self.t
    def advance(self, d): self.t += d


if __name__ == "__main__":
    clock = Clock()
    kv = KVStoreTTL(clock=clock)
    kv.set("session", "abc", ttl=10)
    print("t=0 get:", kv.get("session", None))
    clock.advance(10)
    print("t=10 exists:", kv.exists("session"))
    print("cleanup removed:", kv.cleanup())
