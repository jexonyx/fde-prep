"""Reference — completed idiom exercises. Check AFTER attempting."""


def reverse_string(s):
    return s[::-1]


def drop_first_last(s):
    return s[1:-1]


def word_lengths(words):
    return {w: len(w) for w in words}


def evens(nums):
    return [n for n in nums if n % 2 == 0]


def tally(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def rank_desc(scores):
    return sorted(scores, key=lambda name: (-scores[name], name))
