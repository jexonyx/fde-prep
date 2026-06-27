# 02 — pair-with-target

**Tier 0 · ~20 min.**

## Concepts drilled
Dict-as-lookup (the "have I seen the complement?" pattern), turning an O(n²) scan into O(n),
sets for de-duplication.

## Problem statement
Write `two_sum(nums, target)` that returns a tuple `(i, j)` of two **indices** (`i < j`) such
that `nums[i] + nums[j] == target`. If no such pair exists, return `None`. If several pairs
work, return the one whose second index `j` is smallest (i.e. the first completable pair as
you scan left to right).

## Worked example
```
two_sum([2, 7, 11, 15], 9)   # -> (0, 1)   because 2 + 7 == 9
two_sum([3, 2, 4], 6)        # -> (1, 2)   because 2 + 4 == 6
two_sum([1, 2, 3], 99)       # -> None
```

## Constraints / assumptions
- `nums` is a list of ints (may be negative); `target` is an int.
- Indices, not values. `i < j`.
- One scan; do not use the same element twice.

## Follow-up extensions  → `TestStretch`
1. `all_pairs(nums, target)` — return **all unique value-pairs** that sum to `target`, each as
   a sorted tuple `(small, large)`, the whole list sorted ascending. Duplicates in the input
   must not produce duplicate pairs. No solution → `[]`. A value pairs with itself only if it
   occurs at least twice (`[3, 3], 6 -> [(3, 3)]`).

## Edge cases to consider
- Empty list / single element → `None`.
- No valid pair.
- Duplicate values (`[3, 3], 6`).
- (A couple more hide in `TestStretch` — think negatives and zero.)

## Complexity target
`two_sum`: O(n) time, O(n) space (the seen-map). Be ready to contrast with the naive O(n²)
double loop and say why the map wins.

## Narration prompts
- Before coding: "I'll keep a dict of value→index of everything seen so far; for each new
  number I look up `target - n` in O(1)."
- Say why you store the index, not just the value.
- For the follow-up, note the shift from *indices* to *unique values*, and how a set kills
  the duplicates.
