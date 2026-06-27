# 05 — merge-sorted

**Tier 0 · ~20 min.**

## Concepts drilled
Clean **two-pointer** control flow, the "drain the remainder" tail, preserving duplicates and
stability. This is the last pure-function rust-off before the class work.

## Problem statement
Write `merge(a, b)` that merges two **already-sorted** ascending lists into one sorted list.
Don't just concatenate-and-sort — walk both with two indices in O(n + m). Duplicates are kept
(the result has every element of both inputs).

## Worked example
```
merge([1, 3, 5], [2, 4, 6])   # -> [1, 2, 3, 4, 5, 6]
merge([1, 1, 2], [1, 3])      # -> [1, 1, 1, 2, 3]
merge([], [2, 4])             # -> [2, 4]
```

## Constraints / assumptions
- Both inputs are sorted ascending. Lengths may differ; either may be empty.
- Elements are comparable (ints here). Return a **new** list; don't mutate the inputs.

## Follow-up extensions  → `TestStretch`
1. `merge_k(lists)` — merge **k** sorted lists into one sorted list. `lists` may be empty, may
   contain empty lists, and the lists may have wildly different lengths. (Reusing `merge` is
   fine and shows good composition; be ready to discuss the complexity of the pairwise
   approach vs a heap.)

## Edge cases to consider
- One input empty; both empty.
- Very unequal lengths (one long tail).
- Duplicates across and within the inputs.

## Complexity target
`merge`: O(n + m) time, O(n + m) space. For `merge_k` with k lists totalling N elements, be
ready to state the cost of folding `merge` across them (O(k · N) worst case) versus a
heap-based O(N log k).

## Narration prompts
- "Two pointers, advance whichever front is smaller; `<=` keeps it stable so equal elements
  preserve their relative order."
- Call out the tail: "when one list runs out, extend with the rest of the other — no extra
  comparisons needed."
