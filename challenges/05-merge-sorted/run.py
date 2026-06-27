"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import merge, merge_k

if __name__ == "__main__":
    print("merge([1,3,5], [2,4,6]):", merge([1, 3, 5], [2, 4, 6]))
    print("merge_k([[1,4],[2],[0,3,5]]):", merge_k([[1, 4], [2], [0, 3, 5]]))
