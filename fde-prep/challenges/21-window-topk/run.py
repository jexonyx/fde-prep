"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import WindowTopK

if __name__ == "__main__":
    w = WindowTopK(window_size=3, k=2)
    for item in ["a", "b", "a", "c", "a"]:
        w.add(item)
        print(f"after add({item!r}): top_k = {w.top_k()}")
