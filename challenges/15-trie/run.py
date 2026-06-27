"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import Trie

if __name__ == "__main__":
    t = Trie()
    for w in ["car", "card", "care", "cat", "dog"]:
        t.insert(w)
    print("search('car'):", t.search("car"))
    print("search('ca'):", t.search("ca"))
    print("starts_with('ca'):", t.starts_with("ca"))
    print("autocomplete('car'):", t.autocomplete("car"))
