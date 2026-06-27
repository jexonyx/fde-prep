"""Reference — 03 group-anagrams. Check AFTER attempting."""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


def group_anagrams_normalized(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word.lower().replace(" ", "")))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
