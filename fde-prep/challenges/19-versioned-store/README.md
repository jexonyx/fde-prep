# 19 — versioned-store

**Tier 3 · ~30 min.**

## Concepts drilled
Append-only history per key, indexing into history (snapshots), and **revert as a new
snapshot** (history is never destroyed).

## Problem statement
Build a `VersionedStore`:
- `set(key, value)` — record a new version of `key`. The first `set` for a key is **version
  0**, the next is version 1, and so on.
- `get(key)` — the latest value. `KeyError` if the key was never set.
- `get_at(key, version)` — the value at a specific historical version. `KeyError` if the key
  is unknown; `IndexError` if the version doesn't exist.

## Worked example
```
vs = VersionedStore()
vs.set("a", 1)        # version 0
vs.set("a", 2)        # version 1
vs.get("a")           # -> 2
vs.get_at("a", 0)     # -> 1
vs.get_at("a", 9)     # -> raises IndexError
```

## Constraints / assumptions
- Versions are per-key, 0-based, contiguous.
- Values may repeat; history keeps every `set`, in order.

## Follow-up extensions  → `TestStretch`
1. `revert(key, version)` — set the key's current value back to what it was at `version`.
   Crucially this is **not** a deletion: it appends a *new* version equal to the old value, so
   the full history (including the versions after the reverted point) is preserved and
   `get_at` still returns them. Return the reverted-to value.

## Edge cases to consider
- `get` / `get_at` on an unknown key.
- `get_at` with a negative or too-large version.
- After a `revert`, both the new latest value and the still-intact older versions.

## Complexity target
`set` O(1) amortised, `get` O(1), `get_at` O(1). Space O(total sets) — be ready to mention
that unbounded history is the obvious cost and how you'd cap it.

## Narration prompts
- "Each key maps to a list of values; `set` appends, `get` is `[-1]`, `get_at` indexes."
- For `revert`, stress that it *appends* rather than truncates — "history stays append-only,
  which keeps `get_at` honest."
