# 03 — group-anagrams

**Tier 0 · ~20 min.**

## Concepts drilled
**Tuple keys / sorted signatures in a dict** — the core "give each equivalence class a
canonical key" trick. `dict.setdefault`, insertion-ordered grouping.

## Problem statement
Write `group_anagrams(words)` that groups words which are anagrams of one another. Return a
list of groups (each group a list of the original words). Two words are anagrams if one is a
rearrangement of the other's letters. **Ordering is defined:** groups appear in the order
their first member was seen; within a group, words keep their input order.

## Worked example
```
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Constraints / assumptions
- `words` is a list of strings. The empty string is a valid word (it's its own anagram).
- Case- and space-sensitive for the base version (`"Tea"` and `"eat"` are *not* grouped).

## Follow-up extensions  → `TestStretch`
1. `group_anagrams_normalized(words)` — group **case-insensitively and ignoring spaces**, so
   `"Listen"`, `"silent"`, and `"Tin sel"` all land together. The returned words are still the
   originals (don't lower-case the output), only the grouping key is normalised.

## Edge cases to consider
- Empty list → `[]`; a single word → one group.
- Duplicate words (they go in the same group, both kept).
- The empty string.
- (One more hides in `TestStretch`.)

## Complexity target
O(N · k log k) for N words of max length k (sorting each word to form its key). Be ready to
mention the alternative key — a 26-count tuple — that drops the log k.

## Narration prompts
- Say the signature out loud: "anagrams share the same multiset of letters, so I'll key by
  `tuple(sorted(word))` — a tuple because it's hashable and usable as a dict key."
- Note why you return `list(groups.values())` and how dict insertion order gives you the
  group ordering for free.
