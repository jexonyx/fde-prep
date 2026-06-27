"""Reference — 02 pair-with-target. Check AFTER attempting."""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return (seen[complement], i)
        seen[n] = i
    return None


def all_pairs(nums, target):
    seen = set()
    found = set()
    for n in nums:
        complement = target - n
        if complement in seen:
            found.add((min(n, complement), max(n, complement)))
        seen.add(n)
    return sorted(found)
