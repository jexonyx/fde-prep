# 12 — event-log

**Tier 2 · ~30 min.**

## Concepts drilled
Storing records as tuples, filtering with comprehensions, **inclusive range** semantics,
aggregation into a dict, and a general `query` that composes optional filters.

## Problem statement
Build an `EventLog`:
- `append(timestamp, event_type, payload)` — record an event (timestamps may arrive out of
  order; you store them as given).
- `by_type(event_type)` — events of that type, in insertion order, as `(timestamp, type,
  payload)` tuples.
- `in_range(start, end)` — events with `start <= timestamp <= end` (**inclusive** both ends),
  in insertion order.

## Worked example
```
log = EventLog()
log.append(1, "click", {"x": 10})
log.append(2, "view", {"page": "home"})
log.append(3, "click", {"x": 20})
log.by_type("click")     # -> [(1, "click", {"x": 10}), (3, "click", {"x": 20})]
log.in_range(2, 3)       # -> [(2, "view", {...}), (3, "click", {...})]
```

## Constraints / assumptions
- `timestamp` is comparable (ints here). `event_type` is hashable. `payload` is arbitrary.
- Range is inclusive on both ends. Insertion order is preserved in all query results.

## Follow-up extensions  → `TestStretch`
1. `count_by_type()` — return a dict mapping each event type to how many events it has.
2. `query(event_type=None, start=None, end=None)` — a single method combining the filters;
   any argument left `None` is "don't filter on this." (Reusing it to implement `by_type` /
   `in_range` is a nice composition move.)

## Edge cases to consider
- Empty log; queries that match nothing.
- Range boundaries exactly equal to an event's timestamp (inclusive).
- Out-of-order timestamps on append (results still follow insertion order, not time order —
  unless you decide otherwise; state it).

## Complexity target
`append` O(1). `by_type` / `in_range` / `query` O(n). `count_by_type` O(n).

## Narration prompts
- "Events are `(timestamp, type, payload)` tuples in a list; queries are filters over that
  list — I'll keep insertion order."
- State your range semantics out loud ("inclusive both ends") before coding `in_range`.
- When you add `query`, mention that `by_type`/`in_range` are special cases of it.
