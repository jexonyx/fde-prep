"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import two_sum, all_pairs

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print("nums:", nums)
    print("two_sum(target=9):", two_sum(nums, 9))
    print("all_pairs([1,2,3,2,4], 5):", all_pairs([1, 2, 3, 2, 4], 5))
