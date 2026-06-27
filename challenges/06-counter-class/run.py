"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import Counter

if __name__ == "__main__":
    c = Counter()
    for k in ["apple", "apple", "pear", "apple", "pear", "plum"]:
        c.increment(k)
    print("counts:", {k: c.count(k) for k in ["apple", "pear", "plum"]})
    print("most_common(2):", c.most_common(2))
    c.decrement("plum")
    print("after decrement('plum'), most_common():", c.most_common())
