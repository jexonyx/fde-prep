# 08 — kv-store

**Tier 1 · ~20 min.**

## Concepts drilled
Clean `KeyError`-vs-sentinel-default design, why `None` is a *bad* "missing" signal, the
`object()` sentinel trick, `key in dict`.

## Problem statement
Build an in-memory `KVStore`:
- `set(key, value)` — store/overwrite.
- `get(key)` — return the value; raise `KeyError` if the key is absent.
- `delete(key)` — remove the key; raise `KeyError` if it's absent.
- `exists(key)` — return `True`/`False`.

## Worked example
```
kv = KVStore()
kv.set("a", 1)
kv.get("a")        # -> 1
kv.exists("a")     # -> True
kv.delete("a")
kv.exists("a")     # -> False
kv.get("a")        # -> raises KeyError
```

## Constraints / assumptions
- Any hashable key; any value — **including `None`** (storing `None` is legal and distinct
  from "absent").
- `get`/`delete` on a missing key raise `KeyError`, not return `None`.

## Follow-up extensions  → `TestStretch`
1. `get(key, default)` — when called with a second argument, return `default` for a missing
   key instead of raising. The catch: `default` itself may be `None`, so you can't use `None`
   to detect "no default given." Use a private sentinel (`_MISSING = object()`). The default
   must **not** be inserted into the store.

## Edge cases to consider
- Storing `None` as a value, then `get`/`exists`.
- Overwriting an existing key.
- `get(key, None)` on a missing key vs `get(key)` on a missing key (one returns, one raises).

## Complexity target
All operations O(1) — it's a thin, well-behaved wrapper over a dict. The value is in the
*interface decisions*, not the algorithm.

## Narration prompts
- "I'll signal 'absent' with `KeyError`, not a `None` return, because `None` is a valid stored
  value — conflating them is a classic bug."
- For the follow-up: "I can't default `default=None` because `None` is meaningful, so I use a
  unique sentinel object that no caller can pass."
