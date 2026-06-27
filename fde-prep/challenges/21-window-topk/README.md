# 21 — window-topk

**Tier 3 · ~40 min.** Eviction-heavy — the bookkeeping is the whole challenge.

## Concepts drilled
Maintaining a **bounded sliding window** of the last N events with a queue, keeping a live
**frequency count** as items enter and leave, and extracting a deterministic **top-K** with a
tie-break.

## Problem statement
Build `WindowTopK(window_size, k)`:
- `add(item)` — record `item` as the newest event. Only the **last `window_size` events** are
  retained; adding past that evicts the oldest event and decrements its count.
- `top_k()` — return up to `k` `(item, count)` tuples for the items in the current window,
  ordered by count **descending**, ties broken by **item ascending** (so the result is
  deterministic).

## Worked example
```
w = WindowTopK(window_size=3, k=2)
w.add("a"); w.add("b"); w.add("a")
w.top_k()      # window [a,b,a] -> [("a", 2), ("b", 1)]
w.add("c")     # window [b,a,c] (oldest "a" evicted) -> counts a:1,b:1,c:1
w.top_k()      # -> [("a", 1), ("b", 1)]   (tie broken by item ascending, top 2)
w.add("a")     # window [a,c,a] -> a:2,c:1
w.top_k()      # -> [("a", 2), ("c", 1)]
```

## Constraints / assumptions
- `window_size >= 1`, `k >= 0`. Items are hashable and comparable (for the tie-break).
- When fewer than `k` distinct items exist, return them all.

## Follow-up extensions  → `TestStretch`
1. **Ties + efficiency.** Make the tie-break explicit and correct (item ascending), and be
   ready to discuss complexity: the naive `top_k` sorts all distinct items O(d log d); a heap
   gives O(d log k). State the trade-off; you don't have to implement the heap.

## Edge cases to consider
- `top_k` before the window fills.
- `window_size == 1` (each `add` replaces the whole window).
- Items leaving the window and their count dropping to zero (must disappear, not linger at 0).

## Complexity target
`add` O(1) amortised (append + one eviction). `top_k` O(d log d) for d distinct items in the
window (or O(d log k) with a heap).

## Narration prompts
- "Two structures: a queue for the window order so I know what to evict, and a count dict for
  frequencies. They move together."
- Stress the eviction invariant: "when an item's count hits 0 I delete the key, so stale items
  never show up in `top_k`."
- State the tie-break out loud and why it makes the output deterministic.
