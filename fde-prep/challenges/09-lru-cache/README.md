# 09 — lru-cache

**Tier 1 · ~30 min.** The canonical FDE-adjacent one — expect it or a cousin in the real
round.

## Concepts drilled
Combining a **dict (O(1) lookup)** with an **ordering** (recency); why a plain list for
ordering is O(n) and how an insertion-ordered dict gives you O(1) "move to most-recent."

## Problem statement
Build `LRUCache(capacity)`:
- `get(key)` — return the value and mark the key **most-recently-used**. Raise `KeyError` if
  the key isn't present.
- `put(key, value)` — insert/update the key (also marks it most-recently-used). If this
  exceeds `capacity`, evict the **least-recently-used** key.
- `__contains__` (`key in cache`) — membership test that does **not** affect recency.
- `__len__` — current number of entries.

## Worked example
```
c = LRUCache(2)
c.put("a", 1)
c.put("b", 2)
c.get("a")        # -> 1   (now "a" is most-recent, "b" is LRU)
c.put("c", 3)     # capacity exceeded -> evict "b"
"b" in c          # -> False
c.get("a")        # -> 1   (still there)
c.get("c")        # -> 3
```

## Constraints / assumptions
- `capacity` is a positive int; `LRUCache(0)` or negative raises `ValueError`.
- Updating an existing key via `put` refreshes its recency and does not grow the size.

## Follow-up extensions  → `TestStretch`
1. **O(1) for both `get` and `put`.** A dict gives O(1) lookup; you also need O(1)
   "promote to most-recent" and "find/evict least-recent." Python's insertion-ordered dict
   does this: deleting and re-inserting a key moves it to the end, and the first key in
   iteration order is the LRU. Be ready to discuss the classic alternative (hash map +
   doubly-linked list) and why it's the same Big-O.

## Edge cases to consider
- `capacity == 1` (every `put` of a new key evicts).
- `get` refreshing recency so a *different* key becomes the eviction victim.
- Re-`put`ting an existing key (no eviction, recency refreshed).

## Complexity target
`get` and `put` both O(1). `__len__`/`__contains__` O(1).

## Narration prompts
- "Lookup wants a dict; recency wants an order. I'll lean on the dict *being* insertion-
  ordered: on access I pop-and-reinsert to push the key to the most-recent end."
- Say which end is LRU and which is MRU before you write the eviction line.
- Mention the dict+linked-list version as the 'if dict ordering didn't exist' answer.
