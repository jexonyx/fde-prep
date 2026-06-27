# 06 — counter-class

**Tier 1 · ~25 min.** Your first class. Small, but it sets the pattern for everything after:
state in `__init__`, behaviour in methods, a clean public surface.

## Concepts drilled
`__init__` state, `dict.get` counting inside a class, `sorted(key=)`, **stable sort for
insertion-order tie-breaks**, deciding what "delete vs floor" means.

## Problem statement
Build a `Counter` class:
- `increment(key)` — add 1 to `key`'s count (starting from 0).
- `decrement(key)` — subtract 1. When a count reaches 0 the key is **removed** entirely.
  Decrementing a key that isn't present is a no-op (it does not go negative).
- `count(key)` — the current count, or 0 if absent.
- `most_common(n=None)` — a list of `(key, count)` tuples, highest count first. With `n`,
  return only the top `n`; with no argument, return all.

## Worked example
```
c = Counter()
c.increment("a"); c.increment("a"); c.increment("b")
c.count("a")            # -> 2
c.most_common(1)        # -> [("a", 2)]
c.decrement("b")        # "b" hits 0 -> removed
c.count("b")            # -> 0
```

## Constraints / assumptions
- Keys are hashable. Counts are non-negative; 0 means "not present."
- `most_common` returns a list of tuples, not a dict.

## Follow-up extensions  → `TestStretch`
1. **Tie-breaking by insertion order:** when two keys have the same count, the one first
   inserted (i.e. first seen via `increment`) comes first in `most_common`. A key removed by
   `decrement` and later re-incremented counts as newly inserted (goes to the back of a tie).
   Hint: Python dicts preserve insertion order and `sorted` is stable.

## Edge cases to consider
- `most_common` on an empty counter → `[]`; `most_common(0)` → `[]`.
- Decrement to exactly 0 (removal) and decrement-when-absent.
- (One ordering subtlety hides in `TestStretch`.)

## Complexity target
`increment` / `decrement` / `count`: O(1). `most_common`: O(k log k) for k distinct keys.

## Narration prompts
- "State lives in a dict keyed by item; counting is `get(key, 0) + 1`."
- Decide and *say* your delete-vs-floor rule before coding — interviewers probe this.
- For the follow-up: "sorted is stable, and the dict already holds insertion order, so
  sorting by `-count` alone gives me the tie-break for free."
