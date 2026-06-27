"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import group_anagrams, group_anagrams_normalized

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("words:", words)
    print("group_anagrams:", group_anagrams(words))
    print("normalized(['Listen','silent','Tin sel']):",
          group_anagrams_normalized(["Listen", "silent", "Tin sel"]))
