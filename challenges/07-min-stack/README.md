# 07 — min-stack

**Tier 1 · ~25 min.**

## Concepts drilled
Maintaining an **auxiliary structure** so a normally-O(n) query becomes O(1); the
"track the answer alongside the data" pattern; raising cleanly on invalid operations.

## Problem statement
Build a `MinStack` — a LIFO stack that also reports its minimum in O(1):
- `push(x)` — push a value.
- `pop()` — remove and return the top value.
- `top()` — return (without removing) the top value.
- `get_min()` — return the current minimum of all values on the stack.

**All four are O(1).** Calling `pop`, `top`, or `get_min` on an empty stack raises
`IndexError`.

## Worked example
```
s = MinStack()
s.push(3); s.push(1); s.push(2)
s.get_min()   # -> 1
s.top()       # -> 2
s.pop()       # -> 2
s.get_min()   # -> 1
s.pop()       # -> 1
s.get_min()   # -> 3   (min recovers correctly as values leave)
```

## Constraints / assumptions
- Values are comparable (ints). Duplicates allowed.
- "O(1)" is the whole point — a solution that scans the stack for the min on each call does
  **not** pass the spirit of this exercise (and the stretch tier nudges you on it).

## Follow-up extensions  → `TestStretch`
1. Make `get_min` correct across **duplicate minimums** — pushing the current min twice then
   popping once must still report that min. (The clean fix is to store, alongside each
   element, what the min was at that depth.)

## Edge cases to consider
- Any operation on an empty stack → `IndexError`.
- Duplicated minimum values.
- The min changing (or not) after a pop.

## Complexity target
Every operation O(1) time. O(n) extra space for the auxiliary min-tracking is expected and
fine — be ready to justify that trade.

## Narration prompts
- "The naive `get_min` is O(n); I'll trade space for time by keeping a parallel stack of
  'min so far at this depth', so the current min is always the top of that aux stack."
- Explain why pushing the min onto the aux stack *every* time (not only when it's a new min)
  makes `pop` trivially correct.
