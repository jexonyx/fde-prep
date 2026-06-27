"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import LRUCache

if __name__ == "__main__":
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    print("get('a'):", c.get("a"))   # a now most-recent
    c.put("c", 3)                     # evicts b
    print("'b' in c:", "b" in c)
    print("get('c'):", c.get("c"))
    print("len:", len(c))
