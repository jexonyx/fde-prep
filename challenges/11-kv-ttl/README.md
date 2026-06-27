# 11 — kv-ttl

**Tier 2 · ~30 min.** This extends `08-kv-store`; ideally you reuse its shape rather than
rewrite it.

## Concepts drilled
**Injectable clock** (so time is testable without `sleep`), storing an expiry alongside each
value, **lazy vs active expiry**, the boundary semantics of "expired."

## Problem statement
Build `KVStoreTTL` — a key/value store where entries can expire:
- `__init__(clock=time.time)` — `clock` is a zero-arg callable returning the current time.
  Tests inject a fake so they control time.
- `set(key, value, ttl=None)` — store `value`. If `ttl` is given, the entry expires `ttl`
  time-units after now; `ttl=None` means it never expires.
- `get(key, default=_MISSING)` — return the value if present and not expired; else raise
  `KeyError` (or return `default` if supplied). Reading an expired key treats it as absent.
- `exists(key)` — `True` only if present and unexpired.
- `delete(key)` — remove; `KeyError` if absent or already expired.

An entry is **expired** when `clock() >= expires_at` (valid for `[set_time, set_time + ttl)`).

## Worked example
```
clock = FakeClock(0)              # a callable you can advance
kv = KVStoreTTL(clock=clock)
kv.set("a", 1, ttl=10)
kv.get("a")        # -> 1
clock.advance(10)                 # now == expires_at
kv.get("a")        # -> raises KeyError  (expired)
```

## Constraints / assumptions
- Time is whatever the clock returns (ints in tests). Don't call `time.time()` directly —
  use `self._clock()`.
- `ttl=None` → permanent. `ttl=0` → expires immediately.

## Follow-up extensions  → `TestStretch`
1. **Lazy vs active expiry.** Your reads should expire entries *lazily* (drop them when
   touched). Then add `cleanup()` for *active* expiry: sweep and remove every currently-
   expired entry, returning how many were removed. Be ready to say when each is appropriate.

## Edge cases to consider
- Reading exactly at the expiry instant (`>=`).
- Overwriting a key with `set` — does the TTL reset? (Decide and state it.)
- `delete` on an expired key.

## Complexity target
`get`/`set`/`exists`/`delete` O(1). `cleanup` O(n) in the number of stored keys.

## Narration prompts
- "I store `(value, expires_at)`; `expires_at` is `None` for permanent. Reads check the clock
  and lazily evict."
- Call out *why* an injectable clock matters: "so tests are deterministic and fast — no
  `sleep`, no flakiness."
- Contrast lazy vs active expiry out loud when you add `cleanup`.
