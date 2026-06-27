# 13 — rate-limiter

**Tier 2 · ~30 min.**

## Concepts drilled
Per-key state in a dict, **injectable clock**, the difference between a **fixed window** and a
**sliding window**, and the boundary arithmetic that trips people up.

## Problem statement
Build `RateLimiter(limit, window, clock=time.time)`:
- `allow(user_id) -> bool` using a **fixed window**: time is divided into consecutive windows
  of length `window`; a user may make at most `limit` allowed calls per window. The count
  resets when a new window begins. `allow` records the call when it returns `True`.

## Worked example
```
clock = FakeClock(0)
rl = RateLimiter(limit=2, window=10, clock=clock)
rl.allow("u")   # -> True   (1st in window)
rl.allow("u")   # -> True   (2nd)
rl.allow("u")   # -> False  (limit reached)
clock.advance(10)            # new window starts
rl.allow("u")   # -> True   (count reset)
```

## Constraints / assumptions
- `limit >= 0`, `window > 0`. Windows are aligned to multiples of `window` (window index =
  `int(now // window)`).
- Each `user_id` is rate-limited independently.
- A rejected call (`False`) does **not** consume quota.

## Follow-up extensions  → `TestStretch`
1. `allow_sliding(user_id) -> bool` — a **sliding window**: a call is allowed if fewer than
   `limit` allowed calls happened in the **last `window` time-units** (the half-open interval
   `(now - window, now]`). A timestamp exactly `window` units old has fallen out of the
   window. Keep the fixed-window behaviour working alongside it.

## Edge cases to consider
- The exact window boundary (fixed: does `now == k*window` start a new window? sliding: is a
  call exactly `window` ago still counted?).
- `limit == 0` (always reject).
- Multiple users not interfering.

## Complexity target
Fixed window: O(1) per `allow` (store window index + count per user). Sliding: O(k) per call
to drop stale timestamps, where k is the calls within the window; be ready to discuss a deque
to bound the work.

## Narration prompts
- "Fixed window: I bucket by `now // window` and keep `(window_index, count)` per user;
  crossing into a new index resets the count."
- For sliding: "I keep the timestamps of allowed calls and discard any older than
  `now - window` before counting."
- Say the boundary rule out loud for each — it's the thing they'll poke.
